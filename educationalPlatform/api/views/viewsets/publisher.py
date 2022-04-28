from api.models.publisher import Publisher
from api.serializers.publisher import PublisherSerializer
from rest_framework import viewsets


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
