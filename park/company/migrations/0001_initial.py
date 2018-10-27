# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-10-24 07:34
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.CharField(default=uuid.uuid1, max_length=50, primary_key=True, serialize=False)),
                ('company_name', models.CharField(db_index=True, max_length=32, null=True)),
                ('updated_time', models.DateTimeField(auto_now=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
            ],
            options={
                'db_table': 'Company',
            },
        ),
    ]
