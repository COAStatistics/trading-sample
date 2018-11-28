from django.urls import path

from . import views


urlpatterns = [
    path('trade/', views.TradeListCreateAPIView.as_view(), name='api_trade_cr'),
    path('trade/<int:pk>', views.TradeRetrieveUpdateDestroyAPIView.as_view(), name='api_trade_rud'),
]