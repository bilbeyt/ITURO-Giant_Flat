from django.conf.urls import url
from video.views import PlaylistListView, PlaylistDetailView

urlpatterns = [
    url(r'^$', PlaylistListView.as_view(), name="playlists"),
    url(r'^(?P<slug>[\w-]+)/$', PlaylistDetailView.as_view(), name="playlist_detail"),
]
