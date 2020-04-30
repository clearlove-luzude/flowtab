"""aliyun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import  include, url
from django.contrib import admin
from dnsdata import views
from dnsdata import check_views

urlpatterns = [
    #登录页面
    url(r'admin/', admin.site.urls),
    url(r'^$', views.login, name='login'),
    url(r'^login/$', (views.login), name='login'),
    url(r'^checklogin/$', (views.checklogin), name='checklogin'),
    url(r'^index/$', (views.index), name='index'),
    #欢迎页面 目前未作处理
    url(r'^welcome/$', (views.welcome), name='welcome'),
    #cdn域名图表展示页面
    url(r'^aliyun_info/$', (views.aliyun_info), name='aliyun_info'),
    url(r'^shijie_info/$', (views.shijie_info), name='shijie_info'),
    #监控页面
    url(r'^monitor/$', (views.monitor), name='monitor'),
    #监控添加和修改页面
    url(r'^member_add/$', (views.member_add), name='member_add'),
    url(r'^member_edit/$', (views.member_edit), name='member_edit'),
    #域名接口
    url(r'^DomainName_info/$', (views.DomainName_info), name='DomainName_info'),
    url(r'^DomainName_info_shijie/$', (views.DomainName_info_shijie), name='DomainName_info_shijie'),
    #域名展示数据接口
    url(r'^Get_datas/$', (views.Get_datas), name='Get_datas'),
    url(r'^Get_datas_shijie/$', (views.Get_datas_shijie), name='Get_datas_shijie'),
    # 监控列表数据接口
    url(r'^monitor_info/$', (views.monitor_info), name='monitor_info'),
    #监控添加
    url(r'^monitor_add/$', (views.monitor_add), name='monitor_add'),
    #修改
    url(r'^monitor_edit/$', (views.monitor_edit), name='monitor_edit'),
    #删除
    url(r'^monitor_delete/$', (views.monitor_delete), name='monitor_delete'),
    #监控接口及数据检查更新
    url(r'^flush_check/$', (check_views.flush_check), name='flush_check'),
    #日志页面
    url(r'^check_rizhi/$', (views.check_rizhi), name='check_rizhi'),
    #日志获取接口
    url(r'^check_info/$', (views.check_info), name='check_info'),
    # 日费用统计页面
    url(r'^day_cost/$', (views.day_cost), name='day_cost'),
    # 日费用统计接口
    url(r'^day_cost_api/$', (views.day_cost_api), name='day_cost_api'),
    # 月费用统计页面
    url(r'^m_cost/$', (views.m_cost), name='m_cost'),
    # 月费用统计接口
    url(r'^m_cost_api/$', (views.m_cost_api), name='m_cost_api'),
]
