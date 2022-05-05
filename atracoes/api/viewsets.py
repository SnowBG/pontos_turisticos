from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from atracoes.api.serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    """A ViewSet for Atracoes viewing and editing."""

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
