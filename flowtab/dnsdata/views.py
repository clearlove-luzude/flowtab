from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.urls  import reverse
import json,time,datetime
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http  import HttpResponse,HttpResponseRedirect
from dnsdata.models import Cdn_bpsdata
from dnsdata.models import Cdn_bpsdata
from dnsdata.models import Cdn_trafficdata,Cdn_bpsdata,DomainName_tab,Cdn_lookcloud,DomainName_tab_shijie,Controls,Controls_info,Cdn_lookcloud_flow
from dnsdata.check_views import *
# Create your views here.

try:
    from django.http import JsonResponse
except ImportError:
    from .tool import JsonResponse

def login(request):
    try:
        user = request.user
        auth.logout(request)
    except:
        pass
    return render(request,"login.html")

@login_required
def index(request):
    return render(request,"index.html")

@login_required
def aliyun_info(request):
    return render(request,"aliyun.html")

@login_required
def welcome(request):
    return render(request,"welcome.html")

@login_required
def shijie_info(request):
    return render(request,"shijie.html")

@login_required
def check_rizhi(request):
    return render(request,"check_rizhi.html")

@login_required
def monitor(request):
    return render(request,"monitor.html")

@login_required
def member_add(request):
    return render(request,"member-add.html")

@login_required
def member_edit(request):
    return render(request,"member-edits.html")

def checklogin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    msg_dict = {}
    try:
        user = auth.authenticate(username=username, password=password)
    except auth.DoesNotExist:
        raise Http404("User does not exist")
    if user is not None:
        auth.login(request,user)
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            remote_ip =  request.META['HTTP_X_FORWARDED_FOR']
        else:
            remote_ip = request.META['REMOTE_ADDR']
        accmsg = "Hello %s,welcome to captain!"%username
        msg_dict['accmsg'] = accmsg
    else:
        errmsg = "Hello %s,authentication fails!"%username
        msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


def DomainName_info(request):
    if request.method == 'GET':
        try:
            DomainName = DomainName_tab.objects.values_list('DomainName')
        except:
            lists = []
        msg_dict = {}
        lists = []
        n = 0
        for i in DomainName:
            i = ''.join(i)
            n += 1
            msg_dict = {}
            msg_dict['id'] = n
            msg_dict['name'] = i
            lists.append(msg_dict)
        return HttpResponse(json.dumps(lists), content_type='application/json')


def check_info(request):
    dates = Controls_info.objects.all()
    dataCount = dates.count()  # 数据总数
    lis = []
    for i in dates:
        dict = {}
        dict['域名'] = i.DomainName  # 与前端一一对应，自行设置要展示的字段
        dict['累计次数'] = i.control_count  # 外键字段
        dict['监控值'] = i.control_value  # 外键字段
        dict['报警'] = '报警'
        dict['开始时间'] = i.start_time
        lis.append(dict)
    pageIndex = request.GET.get('page')  # 前台传的值，
    pageSize = request.GET.get('limit')  # 前台传的值
    pageInator = Paginator(lis, pageSize)  # 导入分页模块分页操作，不写前端只展示一页数据，
    contacts = pageInator.page(pageIndex)  # 导入分页模块分页操作，不写前端只展示一页数据，
    res = []
    for i in contacts:
        res.append(i)
    print(res)
    Result = {"code": 0, "msg": "", "count": dataCount, "data": res}
    # json.dumps(Result, cls=DateEncoder)没有时间字段问题可直接返回此代码。有就返回下面代码
    return HttpResponse(json.dumps(Result, cls=DateEncoder), content_type="application/json")

#def check_info(request):
#    if request.method == 'GET':
#        try:
#            info = Controls_info.objects.values_list('DomainName','control_value','control_count','start_time')
#        except:
#            lists = []
#        msg_dict = {}
#        lists = []
#        for i in info:
#            msg_dict = {}
#            msg_dict['name'] = i[0]
#            msg_dict['value'] = i[1]
#            msg_dict['count'] = i[2]
#            msg_dict['time'] = str(i[3])
#            lists.append(msg_dict)
#        return HttpResponse(json.dumps(lists), content_type='application/json')


def DomainName_info_shijie(request):
    if request.method == 'GET':
        try:
            DomainName = DomainName_tab_shijie.objects.values_list('DomainName')
        except:
            lists = []
        msg_dict = {}
        lists = []
        n = 0
        for i in DomainName:
            i = ''.join(i)
            n += 1
            msg_dict = {}
            msg_dict['id'] = n
            msg_dict['name'] = i
            lists.append(msg_dict)
        return HttpResponse(json.dumps(lists), content_type='application/json')



def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value,s)
    return '%sB' % n


@login_required
def Get_datas(request):
    if request.method == 'GET':
        domianname = request.GET.get("domianname")
        datainterval = request.GET.get("datainterval")
        try:
            starttime = request.GET.get("starttime")
            endtime = request.GET.get("endtime")
        except:
            starttime = ''
            endtime = ''
        if starttime == '' and endtime == '':
            starttime = time.strftime("%Y%m%d")
            endtime = time.strftime("%Y%m%d")
        msg_dict = {}
        print(domianname,starttime,endtime)
        date_from = '%s'%starttime + ' 00:00:00'
        date_to = '%s'%endtime + ' 23:59:59'
        try:
            flowdata = Cdn_bpsdata.objects.all().filter(DomainName='%s'%domianname,DataInterval='%s'%datainterval,TimeStamp__range=["%s"%date_from, "%s"%date_to]).values_list('TimeStamp_cst','Value','HttpsValue')
            tradata = Cdn_trafficdata.objects.all().filter(DomainName='%s'%domianname,DataInterval='%s'%datainterval,TimeStamp__range=["%s"%date_from, "%s"%date_to]).values_list('TimeStamp_cst','Value','HttpsValue')
        except:
            status = None
        msg_dict = {}
        flowlists = []
        tralist = []
        flowdata = sorted(flowdata)
        for i in flowdata:
            httpdata = int(i[1].split('.')[0])
            httpsdata = int(i[2].split('.')[0])
            flowlists.append({'times': str(i[0]), 'http': httpdata, 'https': httpsdata})
        tradata = sorted(tradata)
        for i in tradata:
            httpdata = int(i[1].split('.')[0])
            httpsdata = int(i[2].split('.')[0])
            tralist.append({'times': str(i[0]), 'http': httpdata, 'https': httpsdata})
        msg_dict['flow'] = flowlists
        msg_dict['tra'] = tralist
        msg_dicts = {}
        msg_dicts[domianname] = msg_dict
        return HttpResponse(json.dumps(msg_dicts), content_type='application/json')


@login_required
def Get_datas_shijie(request):
    if request.method == 'GET':
        domianname = request.GET.get("domianname")
        datainterval = request.GET.get("datainterval")
        try:
            starttime = request.GET.get("starttime")
            endtime = request.GET.get("endtime")
        except:
            starttime = ''
            endtime = ''
        if starttime == '' and endtime == '':
            starttime = time.strftime("%Y%m%d")
            endtime = time.strftime("%Y%m%d")
        msg_dict = {}
        date_from = '%s'%starttime + ' 00:00:00'
        date_to = '%s'%endtime + ' 23:59:59'
        try:
            flowdata = Cdn_lookcloud.objects.all().filter(DomainName='%s'%domianname,DataInterval='%s'%datainterval,TimeStamp_cst__range=["%s"%date_from, "%s"%date_to]).values_list('TimeStamp_cst','Value')
            flowdata_s = Cdn_lookcloud_flow.objects.all().filter(DomainName='%s'%domianname,DataInterval='%s'%datainterval,TimeStamp_cst__range=["%s"%date_from, "%s"%date_to]).values_list('TimeStamp_cst','Value')
        except:
            status = None
        msg_dict = {}
        flowlists = []
        tralist = []
        flowdata = sorted(flowdata)
        for i in flowdata:
            httpdata = int(i[1].split('.')[0])
            tralist.append({'times': str(i[0]), 'http': httpdata})
        msg_dict['flow'] = flowlists
        msg_dicts = {}
        msg_dicts[domianname] = msg_dict
        flowdata_s = sorted(flowdata_s)
        for i in flowdata_s:
            httpdata = int(i[1].split('.')[0])
            flowlists.append({'times': str(i[0]), 'http': httpdata})
        msg_dict['flow'] = flowlists
        msg_dict['tra'] = tralist
        msg_dicts = {}
        msg_dicts[domianname] = msg_dict
        return HttpResponse(json.dumps(msg_dicts), content_type='application/json')

@login_required
def monitor_add(request):
    if request.method == 'GET':
        id = int(request.GET.get("id"))+1
        domianname = request.GET.get("domianname")
        value = request.GET.get("value")
        jk_name = request.GET.get("jk_name")
        email = request.GET.get("email")
        msg_dict = {}
        try:
            flowdata = Controls.objects.all().filter(DomainName=domianname)
        except Exception as e:
            errmsg = "%s" % e
            msg_dict['errmsg'] = errmsg
        if len(flowdata) == 0:
            try:
                flowdata = Controls(c_id=id,DomainName=domianname,control_value=value,email=email,control_item=jk_name,control_info='%s大于%s info连续三次报警'%(jk_name,value),status='正常',isstart='1')
                flowdata.save()
            except:
                errmsg = "%s" % e
                msg_dict['errmsg'] = errmsg
            accmsg = u"添加成功!"
            msg_dict['accmsg'] = accmsg
        else:
            errmsg = u"监控已存在，不可重复添加!"
            msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


@login_required
def monitor_edit(request):
    if request.method == 'GET':
        id = int(request.GET.get("id"))+1
        domianname = request.GET.get("domianname")
        value = request.GET.get("value")
        jk_name = request.GET.get("jk_name")
        email = request.GET.get("email")
        msg_dict = {}
        try:
            flowdata = Controls.objects.all().filter(DomainName=domianname)
        except Exception as e:
            errmsg = "%s" % e
            msg_dict['errmsg'] = errmsg
        try:
            flowdata = Controls(c_id=id,DomainName=domianname,control_value=value,email=email,control_item=jk_name,control_info='%s大于%s info连续三次报警'%(jk_name,value),status='正常',isstart='1')
            flowdata.save()
            accmsg = u"修改成功!"
            msg_dict['accmsg'] = accmsg
        except:
            errmsg = "%s" % e
            msg_dict['errmsg'] = errmsg

    return HttpResponse(json.dumps(msg_dict), content_type='application/json')


@login_required
def monitor_delete(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        msg_dict = {}
        try:
            flowdata = Controls.objects.all().filter(c_id=id).delete()
            flowdatas = Controls.objects.all().filter(c_id=id)
            if len(flowdatas) == 0:
                accmsg = u"删除成功!"
                msg_dict['accmsg'] = accmsg
            else:
                errmsg = "未删除id为%s" %id
                msg_dict['errmsg'] = errmsg
        except Exception as e:
            errmsg = "%s" % e
            msg_dict['errmsg'] = errmsg
    return HttpResponse(json.dumps(msg_dict), content_type='application/json')

from django.core.paginator import Paginator
@login_required
def monitor_info(request):
    dates = Controls.objects.all()
    dataCount = dates.count()  # 数据总数
    lis = []
    for i in dates:
        dict = {}
        dict['域名'] = i.DomainName  # 与前端一一对应，自行设置要展示的字段
        dict['报警规则'] = i.control_info  # 外键字段
        dict['监控项'] = i.control_item  # 外键字段
        dict['通知对象'] = i.email
        dict['状态'] = i.status
        dict['启用'] = i.isstart
        dict['创建时间'] = i.uptime
        dict['id'] = i.c_id
        lis.append(dict)
    pageIndex = request.GET.get('page')  # 前台传的值，
    pageSize = request.GET.get('limit')  # 前台传的值
    pageInator = Paginator(lis, pageSize)  # 导入分页模块分页操作，不写前端只展示一页数据，
    contacts = pageInator.page(pageIndex)  # 导入分页模块分页操作，不写前端只展示一页数据，
    res = []
    for i in contacts:
        res.append(i)
    print(res)
    Result = {"code": 0, "msg": "", "count": dataCount, "data": res}
    # json.dumps(Result, cls=DateEncoder)没有时间字段问题可直接返回此代码。有就返回下面代码
    return HttpResponse(json.dumps(Result, cls=DateEncoder), content_type="application/json")

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)




