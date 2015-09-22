from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from announce.models import AnnounceList, Announce
from announce.serializers import AnnounceListSerializer, AnnounceSerializer


class AnnounceListRouter(ModelRouter):
    route_name = 'announce-list'
    serializer_class = AnnounceListSerializer
    model = AnnounceList

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()


class AnnounceRouter(ModelRouter):
    route_name = 'announcements'
    serializer_class = AnnounceSerializer
    model = Announce

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['id'])

    def get_query_set(self, **kwargs):
      return self.model.objects.filter(announce_list__id=kwargs['list_id']).order_by("-pub_date")


route_handler.register(AnnounceListRouter)
route_handler.register(AnnounceRouter)
