# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_auto_20151205_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file_encryption',
            new_name='document_file_encryption',
        ),
    ]
