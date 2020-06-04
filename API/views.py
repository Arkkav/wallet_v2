from rest_framework import viewsets
from .models import *
from .serializers import WalletSerializer, TxSerializer
from rest_framework.response import Response


class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()


class TxViewSet(viewsets.ModelViewSet):
    serializer_class = TxSerializer
    queryset = Transaction.objects.all()


class WalletTxsViewSet(viewsets.ViewSet):
    def list(self, request, pk):
        queryset = Transaction.objects.filter(wallet_id=pk)
        serializer = TxSerializer(queryset, many=True)
        return Response(serializer.data)

