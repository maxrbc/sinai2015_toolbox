# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temporal_series', '0002_auto_20150615_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='timevar_type',
            field=models.BooleanField(default=False),
        ),
    ]
