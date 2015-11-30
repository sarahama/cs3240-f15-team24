# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20151128_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportfolder',
            name='folder_group',
        ),
        migrations.AddField(
            model_name='report',
            name='report_group',
            field=models.CharField(default='', max_length=200),
        ),
    ]
