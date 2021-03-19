from rest_framework import filters, viewsets

from .models import Sonnet
from .serializers import SonnetSerializer


class SonnetViewSet(viewsets.ModelViewSet):
    queryset = Sonnet.objects.all()
    serializer_class = SonnetSerializer
    search_fields = ['text']
    filter_backends = (filters.SearchFilter,)

