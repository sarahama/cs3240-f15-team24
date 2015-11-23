# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('document', models.FileField(default='unknown', upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('report_title', models.CharField(max_length=64)),
                ('report_short_description', models.TextField(max_length=500)),
                ('report_long_description', models.TextField(blank=True)),
                ('report_creation_date', models.DateTimeField(verbose_name='date published')),
                ('report_public', models.BooleanField(default=False)),
                ('report_file', models.FileField(upload_to='media')),
                ('report_owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReportFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('folder_title', models.CharField(max_length=200)),
                ('folder_creation_date', models.DateTimeField(verbose_name='date published')),
                ('folder_owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='report',
            field=models.ForeignKey(to='report.Report'),
        ),
    ]
