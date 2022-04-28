from api.models.author import Author
from api.serializers.author import AuthorSerializer
from rest_framework import viewsets


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
