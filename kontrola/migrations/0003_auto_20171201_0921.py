# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-01 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kontrola', '0002_auto_20171201_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kontrola',
            old_name='Nazwa',
            new_name='Podzespół',
        ),
    ]
