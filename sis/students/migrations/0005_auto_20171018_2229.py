# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20171004_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='dne',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='semestercourse',
            name='day',
            field=models.CharField(max_length=3, null=True, choices=[(b'Mon', b'Monday'), (b'Tues', b'Tuesday'), (b'Wed', b'Wednessday'), (b'Thu', b'Thursday'), (b'Fri', b'Friday')]),
        ),
    ]
