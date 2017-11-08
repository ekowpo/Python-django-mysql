# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CourseRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('dateOfBirth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=500)),
                ('postalCode', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='SemesterCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='students.Course')),
                ('lecturer', models.ForeignKey(to='students.Lecturer')),
                ('location', models.ForeignKey(to='students.Location')),
                ('semester', models.ForeignKey(to='students.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('dateOfBirth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=500)),
                ('postalCode', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='courseregistration',
            name='course',
            field=models.ForeignKey(to='students.SemesterCourse'),
        ),
        migrations.AddField(
            model_name='courseregistration',
            name='student',
            field=models.ForeignKey(to='students.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(to='students.Department'),
        ),
        migrations.AlterUniqueTogether(
            name='courseregistration',
            unique_together=set([('student', 'course')]),
        ),
    ]
