# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-10-24 07:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('park1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='park1',
            old_name='company_id1',
            new_name='park_id',
        ),
        migrations.RenameField(
            model_name='park1',
            old_name='company_name',
            new_name='park_name',
        ),
    ]
