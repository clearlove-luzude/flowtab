# Generated by Django 3.0.2 on 2020-03-18 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnsdata', '0001_initial'),
    ]

    operations = [
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
    ]