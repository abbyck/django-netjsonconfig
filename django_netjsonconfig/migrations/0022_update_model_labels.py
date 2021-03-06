# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-12 12:41
from __future__ import unicode_literals

import re

import django.core.validators
import sortedm2m.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0021_netjsonconfig_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='backend',
            field=models.CharField(choices=[('netjsonconfig.OpenWrt', 'OpenWRT/LEDE'), ('netjsonconfig.OpenWisp', 'OpenWISP Firmware 1.x')], help_text='Select <a href="http://netjsonconfig.openwisp.org/en/stable/" target="_blank">netjsonconfig</a> backend', max_length=128, verbose_name='backend'),
        ),
        migrations.AlterField(
            model_name='config',
            name='mac_address',
            field=models.CharField(help_text='primary mac address', max_length=17, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', 32), code='invalid', message='Must be a valid mac address.')]),
        ),
        migrations.AlterField(
            model_name='config',
            name='templates',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text='configuration templates, applied from first to last', related_name='config_relations', to='django_netjsonconfig.Template', verbose_name='templates'),
        ),
        migrations.AlterField(
            model_name='template',
            name='backend',
            field=models.CharField(choices=[('netjsonconfig.OpenWrt', 'OpenWRT/LEDE'), ('netjsonconfig.OpenWisp', 'OpenWISP Firmware 1.x')], help_text='Select <a href="http://netjsonconfig.openwisp.org/en/stable/" target="_blank">netjsonconfig</a> backend', max_length=128, verbose_name='backend'),
        ),
    ]
