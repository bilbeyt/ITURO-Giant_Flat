# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20150917_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='order',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
