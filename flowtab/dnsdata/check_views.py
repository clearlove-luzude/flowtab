from django.http  import HttpResponse,HttpResponseRedirect
import configparser
import json
from itertools import groupby
import pymysql
import datetime,time
import sys,os
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")
path = os.path.abspath(configPath)
conf = configparser.ConfigParser()
conf.read(path)
host=conf.get("mysqld","host")
user=conf.get("mysqld","user")
password=conf.get("mysqld","password")
database=conf.get("mysqld","database")

#生成timeid
def create_id(name,time_id):
    n = 0
    for i in name:
        n = n + ord(i)
    return (n*10000+time_id)

def emails(to_list, zhuti, message_body_utf8):
    msg = MIMEMultipart()
    msg_to_list = to_list
    msg['From'] = 'so_notification@zhipu-inc.com'
    Header(msg_to_list, 'utf-8')
    msg['Subject'] = Header('%s'%zhuti, 'utf-8')
    content = "<h2>各位好：</h2><li><font color='red' size='1000'> %s </font></li>"%message_body_utf8
    part = MIMEText(content,'html','utf-8')
    msg.attach(part)
    #server = smtplib.SMTP()
    server = smtplib.SMTP_SSL('smtp.zhipu-inc.com', 465)
    server.connect('smtp.mxhichina.com')
    server.login('so_notification@zhipu-inc.com','cPsx_bm4an546')
    server.sendmail(msg['from'],msg_to_list, msg.as_string())
    server.quit()

curdate = time.strftime("%Y-%m-%d")
print(curdate)

def test(dicts):
    db = pymysql.connect("%s"%host, "%s"%user, "%s"%password, "%s"%database)
    cursor = db.cursor()
    #sql = "select DomainName from dnsdata_cdn_lookcloud where DomainName = '%s' and TimeStamp_cst > '%s' and Value > %d   "%(dicts['name'],curdate,dicts['value'])
    sql = "select DomainName,TimeStamp_cst,Value from dnsdata_cdn_lookcloud where  TimeStamp_cst > '%s 00:00:00' and DomainName = '%s' and Value > %d  "%(curdate,dicts['name'],dicts['value'])
    #print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    #超标字典
    dict_cb = {}
    # 超标列表
    list_cb = []
    results = sorted(results)
    for i in results:
        list_cb.append({'name':i[0],'time':i[1],'value':i[2]})
    list_time = []
    for i in list_cb:
        timestamp = time.mktime(time.strptime('%s' %i['time'], "%Y-%m-%d %H:%M:%S"))
        i['time'] =  (int(timestamp) / 300)
        list_time.append(i['time'])
    list_time = sorted(list_time)
    fun = lambda x: x[1] - x[0]
    lists = []

    for k, g in groupby(enumerate(list_time), fun):
        lists.append({'name':dicts['name'],'value':[v for i, v in g]})
    n = 0
    k = 0
    for i in range(len(lists)):
        if len(lists[n]['value']) < 3:
            lists.pop(n)
            n = n - 1
        n += 1
    #print(lists)

    for i in lists:
        str = "%s %s次 带宽超过:%s 起始时间:%s"%(i['name'],len(i['value']),dicts['values'],datetime.datetime.fromtimestamp(i['value'][0]*300).strftime("%Y--%m--%d %H:%M:%S"))
        #print("域名:%s 连续:%s次 带宽超过:%s 起始时间:%s"%(i['name'],len(i['value']),dicts['values'],datetime.datetime.fromtimestamp(i['value'][0]*300).strftime("%Y--%m--%d %H:%M:%S")))
        dict_s = {'time_id': create_id(i['name'],i['value'][0]), 'name': i['name'], 'value': dicts['values'], 'count': len(i['value']), 'start_time': datetime.datetime.fromtimestamp(i['value'][0] * 300).strftime("%Y--%m--%d %H:%M:%S")}
        #print(dict_s)
        check_insert(dict_s,str,dicts)


def check_info():
    # 打开数据库连接
    db = pymysql.connect("%s" % host, "%s" % user, "%s" % password, "%s" % database)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select * from dnsdata_controls;"
    #查询列表
    lists = []
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            if row[7] == '1':
                if row[2][-1] == 'G' or row[2][-1] == 'g':
                    values = int(row[2][:-1])*1024*1024*1024
                if row[2][-1] == 'M' or row[2][-1] == 'm':
                    values = int(row[2][:-1] * 1024 * 1024 * 1024)
                lists.append({'name':row[1],'value':values,'values':row[2],'email':row[5]})
    except:
        pass
    # 关闭数据库连接
    for i in lists:
        test(i)
    db.close()

def check_insert(dicts,str,dictss):
    # 打开数据库连接
    db = pymysql.connect("%s" % host, "%s" % user, "%s" % password, "%s" % database)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql1 = "select * from dnsdata_controls_info where timec_id = %d and DomainName = '%s' ;"%(dicts['time_id'],dicts['name'])
    # 执行SQL语句
    cursor.execute(sql1)
    # 获取所有记录列表
    results = cursor.fetchall()
    if len(results) == 0:
        #print(('%s'%dictss['email'],'cdn域名告警邮件','%s'%str))
        #try:
        emails('%s'%dictss['email'],'cdn域名:%s 告警邮件'%dicts['name'],'%s'%str)
        #except Exception as e:
        #    print(e)
        #print(1)
        sql = "insert into dnsdata_controls_info (`timec_id`,`DomainName`,`control_value`,`control_count`,`start_time`,`uptime`) values('%d','%s','%s','%s','%s',now());"%(dicts['time_id'],dicts['name'],dicts['value'],dicts['count'],dicts['start_time'])
        cursor.execute(sql)
        db.commit()
    else:
        #print(2)
        sql2 = "update dnsdata_controls_info set control_count = %s where  timec_id = %d and control_count != %s  and DomainName = '%s' ;"%(dicts['count'],dicts['time_id'],dicts['count'],dicts['name'])
        cursor.execute(sql2)
        db.commit()
    db.close()

check_info()

def flush_check(request):
    curdate = time.strftime("%Y-%m-%d")
    check_info()
    db = pymysql.connect("%s" % host, "%s" % user, "%s" % password, "%s" % database)
    cursor = db.cursor()
    sql1 = "select DomainName from dnsdata_controls_info where uptime > '%s 00:00:00'  ;" %curdate
    #print(sql1)
    # 执行SQL语句
    cursor.execute(sql1)
    # 获取所有记录列表
    results = cursor.fetchall()
    #print(results)
    if len(results) == 0:
        sql2 = "update dnsdata_controls set status = '正常' ; "
        #print(sql2)
        cursor.execute(sql2)
        db.commit()
        pass
    else:
        for i in results:
            sql2 = "update dnsdata_controls set status = '报警' where DomainName = '%s' ; "%i[0]
            print(sql2)
            cursor.execute(sql2)
            db.commit()
    db.close()
    a = {'更新':123}
    return HttpResponse(json.dumps(a), content_type="application/json")