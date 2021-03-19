from django.contrib.auth.models import User
from rest_framework import filters, permissions, viewsets

from .models import Sonnet
from .serializers import SonnetSerializer, UserSerializer


class SonnetViewSet(viewsets.ModelViewSet):
    queryset = Sonnet.objects.all()
    serializer_class = SonnetSerializer
    search_fields = ['text']
    filter_backends = (filters.SearchFilter,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
