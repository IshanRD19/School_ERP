# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-03 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0003_auto_20180303_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='total_marks',
            field=models.IntegerField(),
        ),
    ]
