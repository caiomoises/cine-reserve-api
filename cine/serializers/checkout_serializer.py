from rest_framework import serializers

class CheckoutSerializer(serializers.Serializer):
    session_id = serializers.IntegerField()
    seat_id = serializers.IntegerField()