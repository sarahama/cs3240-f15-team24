# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportfolder',
            name='folder_group',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AddField(
            model_name='reportfolder',
            name='folder_reports',
            field=models.CharField(max_length=1000, default=''),
        ),
    ]
