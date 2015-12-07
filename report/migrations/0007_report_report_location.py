# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0006_auto_20151205_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_location',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
