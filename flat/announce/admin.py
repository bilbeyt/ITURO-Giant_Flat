from django.contrib import admin
from announce.models import AnnounceList, Announce


class AnnounceAdmin(admin.ModelAdmin):
    exclude = ["pub_date","date"]
    list_display = ["content_en", "announce_type", "pub_date", "date"]
    search_fields = ["pub_date"]
    list_filter= ["pub_date", "announce_type"]


class AnnounceListAdmin(admin.ModelAdmin):
    exclude = ["",]
    list_display = ["name"]
    search_fields = ["name"]


admin.site.register(AnnounceList, AnnounceListAdmin)
admin.site.register(Announce, AnnounceAdmin)
