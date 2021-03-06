# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-07 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_remove_classes_classpicture'),
        ('Question_Bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_papers',
            name='for_class',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='teacher.Classes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='createdby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teacher.Teachers'),
            preserve_default=False,
        ),
    ]
