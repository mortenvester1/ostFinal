# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-09 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resres', '0008_auto_20170509_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date',
            field=models.BigIntegerField(default=0),
        ),
    ]
