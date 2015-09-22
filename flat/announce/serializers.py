from swampdragon.serializers.model_serializer import ModelSerializer


class AnnounceListSerializer(ModelSerializer):
    class Meta:
        model = "announce.AnnounceList"
        publish_fields = ("name")


class AnnounceSerializer(ModelSerializer):
    class Meta:
        model = "announce.Announce"
        publish_fields = ("content_en", "content_tr", "announce_type", "date")
