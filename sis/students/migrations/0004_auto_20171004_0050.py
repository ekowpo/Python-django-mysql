# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_semester_semestertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semesterType',
            field=models.CharField(max_length=10, null=True, choices=[(b'F', b'Fall'), (b'S1', b'Summer 1'), (b'S2', b'Summer 2'), (b'W', b'Winter')]),
        ),
    ]
