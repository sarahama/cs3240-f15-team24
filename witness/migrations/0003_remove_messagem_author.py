# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('witness', '0002_messagem_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagem',
            name='author',
        ),
    ]
