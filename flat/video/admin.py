from django.contrib import admin
from video.models import Video, Playlist


class VideoAdmin(admin.ModelAdmin):
    exclude = ["pub_date","url"]
    list_display = ["order", "description", "url"]
    search_fields = ["description"]
    list_filter = ["pub_date"]


class PlaylistAdmin(admin.ModelAdmin):
    exclude = ["slug",]
    list_display = ["name","slug"]
    search_fields = ["name",]
    list_filter = ["pub_date"]


admin.site.register(Video, VideoAdmin)
admin.site.register(Playlist, PlaylistAdmin)
