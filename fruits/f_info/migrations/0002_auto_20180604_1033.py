# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('f_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fruinfo',
            options={'verbose_name': '水果信息', 'verbose_name_plural': '水果信息'},
        ),
        migrations.AlterModelOptions(
            name='frutype',
            options={'verbose_name': '水果分类', 'verbose_name_plural': '水果分类'},
        ),
        migrations.AlterField(
            model_name='fruinfo',
            name='fabstract',
            field=models.CharField(verbose_name='水果描述', max_length=200),
        ),
        migrations.AlterField(
            model_name='fruinfo',
            name='fclick',
            field=models.IntegerField(verbose_name='点击数'),
        ),
        migrations.AlterField(
            model_name='fruinfo',
            name='fdetail',
            field=tinymce.models.HTMLField(verbose_name='详情信息'),
        ),
        migrations.AlterField(
            model_name='fruinfo',
            name='fpic',
            field=models.ImageField(verbose_name='水果图片', upload_to='f_media'),
        ),
        migrations.AlterField(
            model_name='fruinfo',
            name='fprice',
            field=models.DecimalField(verbose_name='价格', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='fruinfo',
            name='fstock',
            field=models.IntegerField(verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='fruinfo',
            name='ftitle',
            field=models.CharField(verbose_name='名称', max_length=20),
        ),
        migrations.AlterField(
            model_name='fruinfo',
            name='ftype',
            field=models.ForeignKey(verbose_name='水果分类', to='f_info.FruType'),
        ),
        migrations.AlterField(
            model_name='fruinfo',
            name='funit',
            field=models.CharField(verbose_name='规格', max_length=20),
        ),
        migrations.AlterField(
            model_name='fruinfo',
            name='isRecommend',
            field=models.BooleanField(verbose_name='是否推荐', default=False),
        ),
        migrations.AlterField(
            model_name='frutype',
            name='ttitle',
            field=models.CharField(verbose_name='类别名称', max_length=20),
        ),
    ]
