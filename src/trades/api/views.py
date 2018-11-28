from rest_framework import generics
from rest_framework import pagination
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from trades import models
from . import serializers


class ThousandPagination(pagination.PageNumberPagination):
    page_size = 1000


class TradeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TradeSerializer
    queryset = models.Trade.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ThousandPagination


class TradeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TradeSerializer
    queryset = models.Trade.objects.all()
    permission_classes = [IsAuthenticated]