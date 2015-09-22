# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0002_auto_20150916_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='announce',
            name='announce_type',
            field=models.CharField(default=1, max_length=25, choices=[(b'organization', b'success'), (b'important', b'danger'), (b'info', b'info')]),
            preserve_default=False,
        ),
    ]
