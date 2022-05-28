from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import permissions
from .models import Generation, Load, Prosumer, Storage
from .serializers import (
    GenerationSerializer,
    LoadSerializer,
    ProsumerSerializer,
    StorageSerializer,
)


class GenerationViewSet(viewsets.ModelViewSet):
    queryset = Generation.objects.all()
    serializer_class = GenerationSerializer
    permission_classes = (
        IsAuthenticated,
        permissions.Generation,
    )


class LoadViewSet(viewsets.ModelViewSet):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer
    permission_classes = (
        IsAuthenticated,
        permissions.Load,
    )


class ProsumerViewSet(viewsets.ModelViewSet):
    queryset = Prosumer.objects.all()
    serializer_class = ProsumerSerializer
    permission_classes = (
        IsAuthenticated,
        permissions.Prosumer,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = (
        IsAuthenticated,
        permissions.Storage,
    )
