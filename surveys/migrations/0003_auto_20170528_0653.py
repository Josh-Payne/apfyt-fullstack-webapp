# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-28 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_auto_20170318_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='style',
            field=models.CharField(blank=True, choices=[('rate', 'Rating'), ('text', 'Text Response'), ('mc', 'Multiple Choice'), ('bool', 'Yes/No'), ('number', 'Scale, 1-10')], max_length=25, null=True),
        ),
    ]
