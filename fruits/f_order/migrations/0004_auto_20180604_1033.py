# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f_order', '0003_evaluate_star'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evaluate',
            options={'verbose_name': '商品评价', 'verbose_name_plural': '商品评价'},
        ),
        migrations.AlterModelOptions(
            name='expressinfo',
            options={'verbose_name': '快递物流', 'verbose_name_plural': '快递物流'},
        ),
        migrations.AlterModelOptions(
            name='logistics',
            options={'verbose_name': '发货信息', 'verbose_name_plural': '发货信息'},
        ),
        migrations.AlterModelOptions(
            name='orderinfo',
            options={'verbose_name': '订单信息', 'verbose_name_plural': '订单信息'},
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='isRemind',
            field=models.BooleanField(verbose_name='是否提醒', default=False),
        ),
        migrations.AlterField(
            model_name='evaluate',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='evaluate',
            name='efruit',
            field=models.ForeignKey(verbose_name='商品名', to='f_info.FruInfo'),
        ),
        migrations.AlterField(
            model_name='evaluate',
            name='euser',
            field=models.ForeignKey(verbose_name='用户名', to='f_user.UserInfo'),
        ),
        migrations.AlterField(
            model_name='evaluate',
            name='star',
            field=models.IntegerField(verbose_name='评分', default=5),
        ),
        migrations.AlterField(
            model_name='evaluate',
            name='value',
            field=models.CharField(verbose_name='评论内容', max_length=1000),
        ),
        migrations.AlterField(
            model_name='expressinfo',
            name='ename',
            field=models.CharField(verbose_name='快递名称', max_length=20),
        ),
        migrations.AlterField(
            model_name='expressinfo',
            name='epy',
            field=models.CharField(verbose_name='快递代码', max_length=20),
        ),
        migrations.AlterField(
            model_name='logistics',
            name='ldate',
            field=models.DateTimeField(auto_now=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='logistics',
            name='lname',
            field=models.ForeignKey(verbose_name='物流名称', to='f_order.ExpressInfo'),
        ),
        migrations.AlterField(
            model_name='logistics',
            name='lnumber',
            field=models.CharField(verbose_name='物流单号', max_length=20),
        ),
        migrations.AlterField(
            model_name='logistics',
            name='order',
            field=models.ForeignKey(verbose_name='订单号', to='f_order.OrderInfo'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='oaddress',
            field=models.CharField(verbose_name='收货地址', max_length=150),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='odate',
            field=models.DateTimeField(auto_now=True, verbose_name='订单时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='onumber',
            field=models.CharField(verbose_name='订单号', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='opaystyle',
            field=models.CharField(verbose_name='付款方式', max_length=20),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='ostatus',
            field=models.IntegerField(verbose_name='订单状态', default=0),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='ototal',
            field=models.DecimalField(verbose_name='订单金额', max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='ouser',
            field=models.ForeignKey(verbose_name='用户名', to='f_user.UserInfo'),
        ),
    ]
