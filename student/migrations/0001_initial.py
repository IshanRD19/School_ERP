# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0004_auto_20171115_0749'),
        ('principal', '0013_auto_20171115_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_login_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=16)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Personal_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Students_2018',
            fields=[
                ('RegistrationNo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ClassSection', models.CharField(default='NA', max_length=3)),
                ('RollNo', models.CharField(default='NA', max_length=3)),
                ('NoOfSubjects', models.IntegerField(default=0)),
                ('AcademicScore', models.IntegerField(default=0)),
                ('ClassRank', models.IntegerField(default=0)),
                ('Index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Personal_Info')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable_2018',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassSection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Classes_2018')),
                ('SubjectCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Subjects')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTableLookUp',
            fields=[
                ('TTID', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('WeekDay', models.CharField(max_length=9)),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='timetable_2018',
            name='TTID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.TimeTableLookUp'),
        ),
    ]
