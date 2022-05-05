from rest_framework.viewsets import ModelViewSet
from localizacao.api.serializers import EnderecoSerializer
from localizacao.models import Endereco


class LocalizacaoViewSet(ModelViewSet):
    """A ViewSet for Localizacao viewing and editing."""

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
