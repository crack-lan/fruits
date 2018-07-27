# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f_order', '0002_evaluate'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluate',
            name='star',
            field=models.IntegerField(default=5),
        ),
    ]
