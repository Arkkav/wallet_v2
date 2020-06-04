from rest_framework import serializers
from .models import *


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'name', 'balance')
        read_only_fields = ['balance']


class TxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'tx_comment', 'tx_date', 'tx_sum', 'wallet')
