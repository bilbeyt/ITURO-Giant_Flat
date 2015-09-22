# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('date', models.TextField(null=True)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='AnnounceList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.AddField(
            model_name='announce',
            name='announce_list',
            field=models.ForeignKey(to='announce.AnnounceList'),
        ),
    ]
