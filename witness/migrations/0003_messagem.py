# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('witness', '0002_reporter_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('author', models.CharField(max_length=40)),
                ('message', models.TextField()),
            ],
        ),
    ]
