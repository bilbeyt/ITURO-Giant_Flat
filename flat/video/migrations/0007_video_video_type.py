# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_auto_20150917_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_type',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
