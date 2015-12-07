# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='report',
        ),
        migrations.AlterField(
            model_name='file',
            name='document',
            field=models.FileField(upload_to='media'),
        ),
    ]
