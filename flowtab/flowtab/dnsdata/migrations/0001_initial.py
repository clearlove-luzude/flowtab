# Generated by Django 3.0.2 on 2020-04-28 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cdn_bpsdata',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='主键id')),
                ('DomainName', models.CharField(max_length=100, verbose_name='域名')),
                ('Value', models.CharField(max_length=100, verbose_name='值')),
                ('HttpsValue', models.CharField(max_length=100, verbose_name='https值')),
                ('RequestId', models.CharField(max_length=100, verbose_name='请求id')),
                ('start_time', models.DateTimeField(verbose_name='utc开始时间')),
                ('end_time', models.DateTimeField(verbose_name='utc结束时间')),
                ('TimeStamp', models.DateTimeField(verbose_name='utc当前时间')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('DataInterval', models.CharField(max_length=100, verbose_name='粒度')),
                ('TimeStamp_cst', models.DateTimeField(null=True, verbose_name='当前时间')),
            ],
        ),
        migrations.CreateModel(
            name='Cdn_lookcloud',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='主键id')),
                ('DomainName', models.CharField(max_length=100, verbose_name='域名')),
                ('Value', models.CharField(max_length=100, verbose_name='值')),
                ('start_time', models.DateTimeField(verbose_name='utc开始时间')),
                ('end_time', models.DateTimeField(verbose_name='utc结束时间')),
                ('TimeStamp', models.DateTimeField(verbose_name='utc当前时间')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('DataInterval', models.CharField(max_length=100, verbose_name='粒度')),
                ('TimeStamp_cst', models.DateTimeField(null=True, verbose_name='当前时间')),
                ('code', models.CharField(max_length=100, verbose_name='code')),
                ('message', models.CharField(max_length=100, verbose_name='信息')),
            ],
        ),
        migrations.CreateModel(
            name='Cdn_lookcloud_flow',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='主键id')),
                ('DomainName', models.CharField(max_length=100, verbose_name='域名')),
                ('Value', models.CharField(max_length=100, verbose_name='值')),
                ('start_time', models.DateTimeField(verbose_name='utc开始时间')),
                ('end_time', models.DateTimeField(verbose_name='utc结束时间')),
                ('TimeStamp', models.DateTimeField(verbose_name='utc当前时间')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('DataInterval', models.CharField(max_length=100, verbose_name='粒度')),
                ('TimeStamp_cst', models.DateTimeField(null=True, verbose_name='当前时间')),
                ('code', models.CharField(max_length=100, verbose_name='code')),
                ('message', models.CharField(max_length=100, verbose_name='信息')),
            ],
        ),
        migrations.CreateModel(
            name='Cdn_trafficdata',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='主键id')),
                ('DomainName', models.CharField(max_length=100, verbose_name='域名')),
                ('Value', models.CharField(max_length=100, verbose_name='值')),
                ('HttpsValue', models.CharField(max_length=100, verbose_name='https值')),
                ('RequestId', models.CharField(max_length=100, verbose_name='请求id')),
                ('start_time', models.DateTimeField(verbose_name='utc开始时间')),
                ('end_time', models.DateTimeField(verbose_name='utc结束时间')),
                ('TimeStamp', models.DateTimeField(verbose_name='utc当前时间')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('DataInterval', models.CharField(max_length=100, verbose_name='粒度')),
                ('TimeStamp_cst', models.DateTimeField(null=True, verbose_name='当前时间')),
            ],
        ),
        migrations.CreateModel(
            name='Controls',
            fields=[
                ('c_id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='主键id')),
                ('DomainName', models.CharField(max_length=100, verbose_name='域名')),
                ('control_value', models.CharField(max_length=100, verbose_name='监控值')),
                ('control_item', models.CharField(max_length=100, verbose_name='监控项')),
                ('control_info', models.CharField(max_length=100, verbose_name='监控信息')),
                ('email', models.CharField(max_length=100, verbose_name='邮箱')),
                ('status', models.CharField(max_length=100, verbose_name='状态')),
                ('isstart', models.CharField(max_length=100, verbose_name='是否启动')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Controls_info',
            fields=[
                ('timec_id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='时间戳id')),
                ('DomainName', models.CharField(max_length=100, verbose_name='域名')),
                ('control_value', models.CharField(max_length=100, verbose_name='监控值')),
                ('control_count', models.CharField(max_length=100, verbose_name='连续次数')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='Domainname_cost',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='主键id')),
                ('Value', models.CharField(max_length=100, verbose_name='')),
                ('RequestId', models.CharField(max_length=100, verbose_name='')),
                ('start_time', models.DateTimeField(verbose_name='utc开始时间')),
                ('end_time', models.DateTimeField(verbose_name='utc结束时间')),
                ('TimeStamp', models.DateTimeField(verbose_name='utc当前时间')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='时间')),
                ('DataInterval', models.CharField(max_length=100, verbose_name='粒度')),
                ('TimeStamp_cst', models.DateTimeField(null=True, verbose_name='当前时间')),
            ],
        ),
        migrations.CreateModel(
            name='DomainName_tab',
            fields=[
                ('name_id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='主键id')),
                ('DomainName', models.CharField(max_length=100, verbose_name='域名')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='DomainName_tab_shijie',
            fields=[
                ('name_id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='主键id')),
                ('DomainName', models.CharField(max_length=100, verbose_name='域名')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
    ]
