# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-01 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrola', '0007_auto_20171201_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrolahardware',
            name='Last_Update',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
