# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0003_announce_announce_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='announce_type',
            field=models.CharField(max_length=25, choices=[(b'success', b'organization'), (b'danger', b'important'), (b'info', b'info')]),
        ),
    ]
