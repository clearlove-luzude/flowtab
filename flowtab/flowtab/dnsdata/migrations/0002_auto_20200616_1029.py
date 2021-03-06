# Generated by Django 3.0.6 on 2020-06-16 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnsdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domainname_yf_cost',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='主键id')),
                ('Value', models.CharField(max_length=100, verbose_name='')),
                ('errorCode', models.CharField(max_length=100, verbose_name='')),
                ('start_time', models.DateTimeField(verbose_name='utc开始时间')),
                ('end_time', models.DateTimeField(verbose_name='utc结束时间')),
                ('code', models.DateTimeField(verbose_name='utc当前时间')),
                ('uptime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('DataInterval', models.CharField(max_length=100, verbose_name='粒度')),
                ('TimeStamp_cst', models.DateTimeField(auto_now=True, null=True, verbose_name='当前时间')),
            ],
        ),
        migrations.AlterField(
            model_name='domainname_cost',
            name='TimeStamp_cst',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='当前时间'),
        ),
    ]
