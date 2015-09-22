from django.views.generic.list import ListView
from video.models import Playlist, Video


class PlaylistDetailView(ListView):
    model = Playlist
    template_name = "video.html"

    def get_context_data(self, **kwargs):
        context = super(PlaylistDetailView, self).get_context_data(**kwargs)
        playlist = Playlist.objects.filter(slug=self.kwargs.get("slug"))
        videos = playlist.values_list("video", flat=True)
        url_lst = Video.objects.filter(pk__in=videos).values_list("url", flat=True)
        context["url_list"] = url_lst
        context["playlist"] = playlist
        return context


class PlaylistListView(ListView):
    model = Playlist
    template_name = "playlist.html"

    def get_context_data(self, **kwargs):
        context = super(PlaylistListView, self).get_context_data(**kwargs)
        context["playlist"] = Playlist.objects.all()
        return context
