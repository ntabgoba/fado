# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fahanda', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='New',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
