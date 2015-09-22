# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('content', models.FileField(upload_to=b'video/')),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='video',
            field=models.ManyToManyField(to='video.Video'),
        ),
    ]
