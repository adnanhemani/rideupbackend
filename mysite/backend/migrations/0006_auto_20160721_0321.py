# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_event_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='users_attending_requests',
            field=models.ManyToManyField(to='backend.EventRequests', blank=True),
        ),
        migrations.AlterField(
            model_name='eventridegroup',
            name='riders',
            field=models.ManyToManyField(related_name='eventridegroup_requests_created', to='backend.User', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='backend.Group', blank=True),
        ),
    ]
