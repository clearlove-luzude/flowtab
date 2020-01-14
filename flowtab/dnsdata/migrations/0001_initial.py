# Generated by Django 3.0.2 on 2020-01-09 03:43

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
                ('start_time', models.CharField(max_length=100, verbose_name='utc开始时间')),
                ('end_time', models.CharField(max_length=100, verbose_name='utc结束时间')),
                ('TimeStamp', models.CharField(max_length=100, verbose_name='utc当前时间')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('DataInterval', models.CharField(max_length=100, verbose_name='粒度')),
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
                ('start_time', models.CharField(max_length=100, verbose_name='utc开始时间')),
                ('end_time', models.CharField(max_length=100, verbose_name='utc结束时间')),
                ('TimeStamp', models.CharField(max_length=100, verbose_name='utc当前时间')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('DataInterval', models.CharField(max_length=100, verbose_name='粒度')),
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
    ]
