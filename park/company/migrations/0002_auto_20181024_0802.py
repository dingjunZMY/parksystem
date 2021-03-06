# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-10-24 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default=uuid.uuid1, max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]
