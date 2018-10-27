# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-10-26 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20181024_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='0e6a0f62d8c611e8bb87000c29ca37dd', max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(db_index=True, max_length=50, null=True),
        ),
    ]
