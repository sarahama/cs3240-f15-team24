# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('witness', '0004_messagem_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporter',
            name='public_key',
            field=models.CharField(max_length=1000, default='blank'),
        ),
    ]
