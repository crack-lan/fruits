# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f_info', '0001_initial'),
        ('f_user', '__first__'),
        ('f_order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluate',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('value', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now=True)),
                ('efruit', models.ForeignKey(to='f_info.FruInfo')),
                ('euser', models.ForeignKey(to='f_user.UserInfo')),
            ],
        ),
    ]
