# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_auto_20150917_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='order',
            field=models.PositiveIntegerField(),
        ),
    ]
