from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """A ViewSet for PontoTuristico viewing and editing."""

    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
