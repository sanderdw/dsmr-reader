# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 15:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PVOutputAddStatusSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('export', models.BooleanField(default=False, help_text='Whether the system uploads consumption using the Add Status Service API call.', verbose_name='Enabled')),
                ('upload_interval', models.IntegerField(choices=[(5, '5 minutes'), (10, '10 minutes'), (15, '15 minutes')], default=5, help_text='The interval between each upload (in minutes). Please make sure this matches the device settings.', verbose_name='Upload interval')),
                ('upload_delay', models.IntegerField(default=0, help_text='An artificial delay in uploading data to PVOutput. E.g.: When you set this to "5" and the application uploads the data at 10:45, then only data between 0:00 and 10:40 will be taken into account for upload at that moment. It effectively limits its upload data search by "X minutes ago".', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)], verbose_name='Upload delay (minutes)')),
                ('processing_delay', models.IntegerField(blank=True, default=None, help_text='[!]: This feature is ONLY available when you have a DONATOR account for PVOutput.org! Leave EMPTY to disable the feature. This parameter allows the processing of the data to be delayed, by the specified number of minutes. Allowed values: empty or 0 to 120 (minutes)', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)], verbose_name='PVOutput: Processing delay (minutes)')),
                ('next_export', models.DateTimeField(blank=True, default=None, help_text='Timestamp of the next export. Automatically updated by application.', null=True, verbose_name='Next export')),
            ],
            options={
                'verbose_name': 'PVOutput: Add Status configuration',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='PVOutputAPISettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(blank=True, default=None, help_text='The API key for your PVOutput account. Listed in PVOutput at Settings -> "API Settings".', max_length=256, null=True, verbose_name='API key')),
                ('system_identifier', models.CharField(blank=True, default=None, help_text='The "System ID" for your device. Listed in PVOutput at Settings -> "Registered Systems".', max_length=32, null=True, verbose_name='System ID (digit)')),
            ],
            options={
                'verbose_name': 'PVOutput: API configuration',
                'default_permissions': (),
            },
        ),
    ]
