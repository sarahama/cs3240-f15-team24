# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20151105_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='report_long_descpription',
            new_name='report_long_description',
        ),
        migrations.RemoveField(
            model_name='file',
            name='file_name',
        ),
        migrations.AddField(
            model_name='file',
            name='document',
            field=models.FileField(upload_to='documents/%Y/%m/%d', default='unknown'),
        ),
        migrations.AddField(
            model_name='report',
            name='report_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reportfolder',
            name='folder_owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
