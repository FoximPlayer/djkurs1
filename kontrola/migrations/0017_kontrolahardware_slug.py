# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 08:56
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify

import string
import random

def id_generator():
    size=16
    chars=string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))


def slugify_title(apps, schema_editor):
    '''
    We can't import the Post model directly as it may be a newer
    version than this migration expects. We use the historical version.
    '''
    KontrolaHardware = apps.get_model('kontrola', 'KontrolaHardware')
    for o in KontrolaHardware.objects.all():
        o.slug = slugify(o.podzespół)
        o.save()


class Migration(migrations.Migration):

    dependencies = [
        ('kontrola', '0016_kontrolahardware_slug'),
    ]

    operations = [
        migrations.RunPython(slugify_title),
    ]
