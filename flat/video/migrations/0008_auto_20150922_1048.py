# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_video_video_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_type',
            field=models.CharField(max_length=5, choices=[(b'mp4', b'mp4'), (b'webm', b'webm'), (b'ogg', b'ogg')]),
        ),
    ]
