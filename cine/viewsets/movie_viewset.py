from rest_framework.viewsets import ModelViewSet
from ..models import Movie
from ..serializers import MovieSerializer
# Autenticação e permissão
from rest_framework.permissions import IsAuthenticated


class MovieViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer