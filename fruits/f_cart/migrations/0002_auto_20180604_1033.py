# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f_cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frucart',
            options={'verbose_name': '购物车', 'verbose_name_plural': '购物车'},
        ),
        migrations.AlterField(
            model_name='frucart',
            name='cfruit',
            field=models.ForeignKey(verbose_name='商品名称', to='f_info.FruInfo'),
        ),
        migrations.AlterField(
            model_name='frucart',
            name='count',
            field=models.IntegerField(verbose_name='商品数量'),
        ),
        migrations.AlterField(
            model_name='frucart',
            name='cuser',
            field=models.ForeignKey(verbose_name='用户名', to='f_user.UserInfo'),
        ),
    ]
