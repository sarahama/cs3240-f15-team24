# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('witness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporter',
            name='name',
            field=models.CharField(default='nameless', max_length=50),
        ),
    ]
