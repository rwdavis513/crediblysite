# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20151107_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='job_title',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
