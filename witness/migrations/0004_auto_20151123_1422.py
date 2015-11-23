# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('witness', '0003_messagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagem',
            old_name='author',
            new_name='reader',
        ),
    ]
