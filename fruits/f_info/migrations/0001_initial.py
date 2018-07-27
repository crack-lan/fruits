# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FruInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ftitle', models.CharField(max_length=20)),
                ('fprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('fdetail', tinymce.models.HTMLField()),
                ('fpic', models.ImageField(upload_to='f_media')),
                ('isDelete', models.BooleanField(default=False)),
                ('funit', models.CharField(max_length=20)),
                ('fclick', models.IntegerField()),
                ('fabstract', models.CharField(max_length=200)),
                ('fstock', models.IntegerField()),
                ('isRecommend', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FruType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='fruinfo',
            name='ftype',
            field=models.ForeignKey(to='f_info.FruType'),
        ),
    ]
