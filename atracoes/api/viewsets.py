from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer
import django_filters.rest_framework as filters

class AtracaoViewSet(ModelViewSet, generics.ListAPIView):
    """A ViewSet for Atracoes viewing and editing."""

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_fields = ('nome', 'descricao')
