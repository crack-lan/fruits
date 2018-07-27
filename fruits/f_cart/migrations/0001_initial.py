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
            name='FruCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('count', models.IntegerField()),
                ('cfruit', models.ForeignKey(to='f_info.FruInfo')),
                ('cuser', models.ForeignKey(to='f_user.UserInfo')),
            ],
        ),
    ]
