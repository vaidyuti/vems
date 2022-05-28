from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import permissions
from .models import P2PTransaction
from .serializers import P2PTransactionSerializer


class P2PTransactionViewSet(viewsets.ModelViewSet):
    queryset = P2PTransaction.objects.all()
    serializer_class = P2PTransactionSerializer
    permission_classes = (
        IsAuthenticated,
        permissions.P2PTransaction,
    )
