from rest_framework import serializers
from .models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id', 'scrip_name', 'trade_date', 'quantity', 'price', 'trade_value', 'order_type')
