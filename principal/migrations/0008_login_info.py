# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-11 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_auto_20171111_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=16)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Personal_Info')),
            ],
        ),
    ]
