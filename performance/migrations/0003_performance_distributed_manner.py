# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0002_auto_20170305_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='distributed_manner',
            field=models.CharField(choices=[('data paralel', 'data paralel'), ('model paralel', 'model paralel')], default='data paralel', max_length=100),
        ),
    ]
