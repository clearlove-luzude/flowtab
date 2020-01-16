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
