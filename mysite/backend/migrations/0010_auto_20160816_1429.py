# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_auto_20160816_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='users_attending_requests',
        ),
        migrations.AddField(
            model_name='eventrequests',
            name='event',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='backend.Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='group',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backend.Group'),
        ),
    ]
