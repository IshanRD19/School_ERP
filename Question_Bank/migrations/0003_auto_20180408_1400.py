# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-08 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20180407_0223'),
        ('Question_Bank', '0002_auto_20180407_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.Personal_Info'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questions',
            name='createdby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Personal_Info'),
        ),
    ]
