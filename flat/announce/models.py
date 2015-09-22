from django.db import models
from swampdragon.models import SelfPublishModel
from announce.serializers import AnnounceListSerializer, AnnounceSerializer
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime


announce_type = (
    ("success", "organization"),
    ("danger", "important"),
    ("info", "info")
)


class AnnounceList(SelfPublishModel, models.Model):
    serializer_class = AnnounceListSerializer
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Announce(SelfPublishModel, models.Model):
    serializer_class = AnnounceSerializer
    announce_list = models.ForeignKey(AnnounceList)
    announce_type = models.CharField(choices=announce_type, max_length=25)
    content_en = models.CharField(max_length=100)
    content_tr = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=datetime.now)
    date = models.TextField(null=True)

    def __unicode__(self):
        return self.content_en


@receiver(pre_save,sender=Announce)
def date_handler(sender,instance,*args,**kwargs):
    instance.date = instance.pub_date.isoformat()
