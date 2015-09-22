# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20150917_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='order',
            field=models.PositiveIntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
