from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path


router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='user')
router.register(r'txs', TxViewSet, basename='user')

urlpatterns = [
    path(r'wallets/<int:pk>/txs/', WalletTxsViewSet.as_view({'get': 'list'}), name='wallet_txs'),
]

urlpatterns += router.urls
