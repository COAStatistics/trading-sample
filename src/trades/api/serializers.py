from rest_framework import serializers

from trades import models


class TradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Trade
        fields = '__all__'
