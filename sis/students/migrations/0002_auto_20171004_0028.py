# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='endDate',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='semester',
            name='startDate',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
