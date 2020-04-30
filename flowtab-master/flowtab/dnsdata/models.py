from django.db import models

# Create your models here.
class Cdn_bpsdata(models.Model):
    id = models.CharField(verbose_name='主键id',max_length=15,unique=True,primary_key=True)
    DomainName = models.CharField(verbose_name='域名',max_length=100)
    Value = models.CharField(verbose_name='值',max_length=100)
    HttpsValue = models.CharField(verbose_name='https值',max_length=100)
    RequestId = models.CharField(verbose_name='请求id',max_length=100)
    start_time = models.DateTimeField(verbose_name='utc开始时间')
    end_time = models.DateTimeField(verbose_name='utc结束时间')
    TimeStamp = models.DateTimeField(verbose_name='utc当前时间')
    uptime =  models.DateTimeField('更新时间',auto_now=True)
    DataInterval = models.CharField(verbose_name='粒度',max_length=100)
    TimeStamp_cst = models.DateTimeField(verbose_name='当前时间',null=True)
    def __unicode__(self):
        return self.id

class Cdn_trafficdata(models.Model):
    id = models.CharField(verbose_name='主键id',max_length=15,unique=True,primary_key=True)
    DomainName = models.CharField(verbose_name='域名',max_length=100)
    Value = models.CharField(verbose_name='值',max_length=100)
    HttpsValue = models.CharField(verbose_name='https值',max_length=100)
    RequestId = models.CharField(verbose_name='请求id',max_length=100)
    start_time = models.DateTimeField(verbose_name='utc开始时间')
    end_time = models.DateTimeField(verbose_name='utc结束时间')
    TimeStamp = models.DateTimeField(verbose_name='utc当前时间')
    uptime =  models.DateTimeField('更新时间',auto_now=True)
    DataInterval = models.CharField(verbose_name='粒度',max_length=100)
    TimeStamp_cst = models.DateTimeField(verbose_name='当前时间',null=True)
    def __unicode__(self):
        return self.id

class DomainName_tab(models.Model):
    name_id = models.CharField(verbose_name='主键id',max_length=15,unique=True,primary_key=True)
    DomainName = models.CharField(verbose_name='域名',max_length=100)
    uptime =  models.DateTimeField('更新时间',auto_now=True)
    def __unicode__(self):
        return self.name_id

class DomainName_tab_shijie(models.Model):
    name_id = models.CharField(verbose_name='主键id', max_length=15, unique=True, primary_key=True)
    DomainName = models.CharField(verbose_name='域名', max_length=100)
    uptime = models.DateTimeField('更新时间', auto_now=True)
    def __unicode__(self):
        return self.name_id

class Cdn_lookcloud(models.Model):
    id = models.CharField(verbose_name='主键id',max_length=15,unique=True,primary_key=True)
    DomainName = models.CharField(verbose_name='域名',max_length=100)
    Value = models.CharField(verbose_name='值',max_length=100)
    start_time = models.DateTimeField(verbose_name='utc开始时间')
    end_time = models.DateTimeField(verbose_name='utc结束时间')
    TimeStamp = models.DateTimeField(verbose_name='utc当前时间')
    uptime =  models.DateTimeField('更新时间',auto_now=True)
    DataInterval = models.CharField(verbose_name='粒度',max_length=100)
    TimeStamp_cst = models.DateTimeField(verbose_name='当前时间',null=True)
    code = models.CharField(verbose_name='code',max_length=100)
    message = models.CharField(verbose_name='信息',max_length=100)
    def __unicode__(self):
        return self.id

class Cdn_lookcloud_flow(models.Model):
    id = models.CharField(verbose_name='主键id',max_length=15,unique=True,primary_key=True)
    DomainName = models.CharField(verbose_name='域名',max_length=100)
    Value = models.CharField(verbose_name='值',max_length=100)
    start_time = models.DateTimeField(verbose_name='utc开始时间')
    end_time = models.DateTimeField(verbose_name='utc结束时间')
    TimeStamp = models.DateTimeField(verbose_name='utc当前时间')
    uptime =  models.DateTimeField('更新时间',auto_now=True)
    DataInterval = models.CharField(verbose_name='粒度',max_length=100)
    TimeStamp_cst = models.DateTimeField(verbose_name='当前时间',null=True)
    code = models.CharField(verbose_name='code',max_length=100)
    message = models.CharField(verbose_name='信息',max_length=100)
    def __unicode__(self):
        return self.id



class Controls(models.Model):
    c_id = models.CharField(verbose_name='主键id', max_length=15, unique=True, primary_key=True)
    DomainName = models.CharField(verbose_name='域名', max_length=100)
    control_value = models.CharField(verbose_name='监控值',max_length=100)
    control_item = models.CharField(verbose_name='监控项', max_length=100)
    control_info = models.CharField(verbose_name='监控信息', max_length=100)
    email = models.CharField(verbose_name='邮箱', max_length=100)
    status = models.CharField(verbose_name='状态', max_length=100)
    isstart = models.CharField(verbose_name='是否启动', max_length=100)
    uptime =  models.DateTimeField('更新时间',auto_now=True)

    def __unicode__(self):
        return self.c_id

class Controls_info(models.Model):
    timec_id = models.CharField(verbose_name='时间戳id', max_length=15, unique=True, primary_key=True)
    DomainName = models.CharField(verbose_name='域名', max_length=100)
    control_value = models.CharField(verbose_name='监控值',max_length=100)
    control_count = models.CharField(verbose_name='连续次数', max_length=100)
    start_time = models.DateTimeField(verbose_name='开始时间')
    uptime = models.DateTimeField('更新时间', auto_now=True)
    def __unicode__(self):
        return self.timec_id

class Domainname_cost(models.Model):
    id = models.CharField(verbose_name='主键id', max_length=15, unique=True, primary_key=True)
    Value = models.CharField(verbose_name='', max_length=100)
    RequestId = models.CharField(verbose_name='', max_length=100)
    start_time = models.DateTimeField(verbose_name='utc开始时间')
    end_time = models.DateTimeField(verbose_name='utc结束时间')
    TimeStamp = models.DateTimeField(verbose_name='utc当前时间')
    uptime = models.DateTimeField('更新时间', auto_now=True)
    time = models.DateTimeField('时间', auto_now=True)
    DataInterval = models.CharField(verbose_name='粒度', max_length=100)
    TimeStamp_cst = models.DateTimeField(verbose_name='当前时间',null=True,auto_now=True)
    def __unicode__(self):
        return self.id