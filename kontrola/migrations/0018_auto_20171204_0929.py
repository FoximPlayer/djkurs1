# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kontrola', '0017_kontrolahardware_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kontrolahardware',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
