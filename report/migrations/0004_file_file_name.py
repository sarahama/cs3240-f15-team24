# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20151204_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_name',
            field=models.TextField(default='', max_length=500),
        ),
    ]
