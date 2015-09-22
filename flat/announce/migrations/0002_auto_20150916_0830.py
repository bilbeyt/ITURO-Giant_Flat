# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announce',
            old_name='content',
            new_name='content_en',
        ),
        migrations.AddField(
            model_name='announce',
            name='content_tr',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
