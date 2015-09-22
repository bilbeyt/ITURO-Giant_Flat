from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Video(models.Model):
    description = models.TextField()
    order = models.PositiveIntegerField()
    pub_date = models.DateField(auto_now_add=True)
    content = models.FileField(upload_to = "video/")
    url = models.URLField()


    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        super(Video, self).save(*args,**kwargs)
        self.url = "media/%s" % self.content.name
        super(Video, self).save(*args,**kwargs)


class Playlist(models.Model):
    name = models.CharField(max_length=60)
    pub_date = models.DateField(auto_now_add=True)
    video = models.ManyToManyField(Video)
    slug = models.SlugField(max_length=60)

    def __unicode__(self):
        return self.name


@receiver(pre_save,sender=Playlist)
def playlist_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.name)
