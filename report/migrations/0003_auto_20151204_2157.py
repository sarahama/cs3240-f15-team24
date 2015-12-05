# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20151204_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='report_file',
        ),
        migrations.AddField(
            model_name='report',
            name='report_files',
            field=models.CharField(default='', max_length=500),
        ),
    ]
