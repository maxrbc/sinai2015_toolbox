# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temporal_series', '0003_graph_timevar_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graph',
            name='timevar_type',
        ),
    ]
