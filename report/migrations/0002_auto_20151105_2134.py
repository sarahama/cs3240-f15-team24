# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('witness', '0001_initial'),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('file_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ReportFolder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('folder_title', models.CharField(max_length=200)),
                ('folder_creation_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='pub_date',
            new_name='report_creation_date',
        ),
        migrations.RemoveField(
            model_name='report',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='report',
            name='title',
        ),
        migrations.AddField(
            model_name='report',
            name='report_long_descpription',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='report',
            name='report_owner',
            field=models.ForeignKey(to='witness.Reporter', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='report_short_description',
            field=models.TextField(max_length=500, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='report_title',
            field=models.CharField(max_length=64, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportfolder',
            name='folder_owner',
            field=models.ForeignKey(to='witness.Reporter'),
        ),
        migrations.AddField(
            model_name='file',
            name='report',
            field=models.ForeignKey(to='report.Report'),
        ),
    ]
