# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-10-25 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park1', '0004_auto_20181025_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park1',
            name='park_id',
            field=models.CharField(default='e2804740d84811e8ae70000c29ca37dd', max_length=200, primary_key=True, serialize=False),
        ),
    ]
