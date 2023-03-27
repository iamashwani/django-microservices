from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'user_id', 'amount', 'date')
        read_only_fields = ('id', 'date')