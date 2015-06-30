# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temporal_series', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='subjectID',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graph',
            name='timevar',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
