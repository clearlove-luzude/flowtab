
from django.db.models import Sum

import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aliyun.settings")# project_name 项目名称
django.setup()
from dnsdata.models import Cdn_trafficdata ,Cdn_bpsdata
import json,datetime,time

def monitorinfos_json():
    try:
        domainname = 'gsearchdl.gionee.com'
        #date_from = datetime.datetime(int(2020),int(1),int(4),0,0)
        #date_to = datetime.datetime(int(2020),int(1),int(6),0,0)
        date_from = '2020-01-05' + ' 00:00:00'
        date_to = '2020-01-05' + ' 23:59:59'
        flowdata = Cdn_bpsdata.objects.all().filter(DomainName='gsearchdl.gionee.com',TimeStamp__range=["%s"%date_from, "%s"%date_to]).values_list('TimeStamp','Value','HttpsValue')
        tradata = Cdn_trafficdata.objects.all().filter(DomainName='gsearchdl.gionee.com',TimeStamp__range=["%s"%date_from, "%s"%date_to]).values_list('TimeStamp','Value','HttpsValue')

    except:
        status = None
    msg_dict = {}
    flowlists = []
    tralist = []
    n= 0
    for i in flowdata:
        #print(i[0],i[1],i[2])
        flowlists.append({'times':str(i[0]),'http':i[1],'https':i[2]})
    for i in tradata:
        #print(i[0], i[1], i[2])
        tralist.append({'times': str(i[0]), 'http': i[1], 'https': i[2]})

    msg_dict['flow'] = flowlists
    msg_dict['tra'] = tralist
    msg_dicts = {}
    msg_dicts[domainname] = msg_dict
    print(msg_dicts)

def Get_datas():
    a = True
    if a == True:
        #domianname = request.GET.get("domianname")
        domianname = 'gsearchdl.gionee.com'
        try:
            #starttime = request.POST.get("starttime")
            #endtime = request.POST.get("endtime")
            starttime = '2020-01-01'
            endtime = '2020-01-05'
        except:
            starttime = ''
            endtime = ''
        if len(starttime) <2 and len(endtime) < 2:
            starttime = time.strftime("%Y%m%d")
            endtime = time.strftime("%Y%m%d")
        msg_dict = {}
        #date_from = datetime.datetime(int(2020),int(1),int(4),0,0)
        #date_to = datetime.datetime(int(2020),int(1),int(6),0,0)
        date_from = '%s'%starttime + ' 00:00:00'
        date_to = '%s'%endtime + ' 23:59:59'
        try:
            flowdata = Cdn_bpsdata.objects.all().filter(DomainName='gsearchdl.gionee.com',TimeStamp__range=["%s"%date_from, "%s"%date_to]).values_list('TimeStamp','Value','HttpsValue')
            tradata = Cdn_trafficdata.objects.all().filter(DomainName='gsearchdl.gionee.com',TimeStamp__range=["%s"%date_from, "%s"%date_to]).values_list('TimeStamp','Value','HttpsValue')
        except:
            status = None
        msg_dict = {}
        flowlists = []
        tralist = []
        for i in flowdata:
        #print(i[0],i[1],i[2])
            flowlists.append({'times':str(i[0]),'http':i[1],'https':i[2]})
        for i in tradata:
        #print(i[0], i[1], i[2])
            tralist.append({'times': str(i[0]), 'http': i[1], 'https': i[2]})

        msg_dict['flow'] = flowlists
        msg_dict['tra'] = tralist
        msg_dicts = {}
        msg_dicts[domianname] = msg_dict
        print(json.dumps(msg_dicts))
        #return HttpResponse(json.dumps(msg_dicts), content_type='application/json')

print(Get_datas())