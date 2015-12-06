# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_file_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='report_file_encryption',
        ),
        migrations.AddField(
            model_name='file',
            name='file_encryption',
            field=models.BooleanField(default=False),
        ),
    ]
