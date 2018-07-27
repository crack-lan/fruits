# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f_user', '__first__'),
        ('f_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpressInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ename', models.CharField(max_length=20)),
                ('epy', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Logistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lnumber', models.CharField(max_length=20)),
                ('ldate', models.DateTimeField(auto_now=True)),
                ('is_Delete', models.BooleanField(default=False)),
                ('lname', models.ForeignKey(to='f_order.ExpressInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('count', models.IntegerField()),
                ('fruit', models.ForeignKey(to='f_info.FruInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('onumber', models.CharField(serialize=False, primary_key=True, max_length=20)),
                ('odate', models.DateTimeField(auto_now=True)),
                ('ostatus', models.IntegerField(default=0)),
                ('opaystyle', models.CharField(max_length=20)),
                ('ototal', models.DecimalField(max_digits=6, decimal_places=2)),
                ('oaddress', models.CharField(max_length=150)),
                ('ouser', models.ForeignKey(to='f_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(to='f_order.OrderInfo'),
        ),
        migrations.AddField(
            model_name='logistics',
            name='order',
            field=models.ForeignKey(to='f_order.OrderInfo'),
        ),
    ]
