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
from dnsdata.models import Cdn_trafficdata,Cdn_bpsdata,DomainName_tab
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
def welcome1(request):
    return render(request,"test.html")

@login_required
def welcome(request):
    return render(request,"welcome.html")


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





