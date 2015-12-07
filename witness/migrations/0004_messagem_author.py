# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('witness', '0003_remove_messagem_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagem',
            name='author',
            field=models.CharField(max_length=50, default='nameless'),
        ),
    ]
