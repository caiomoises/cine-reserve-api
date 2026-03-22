from rest_framework import serializers
from ..models import Reservation, Session, User


class ReserveSeatSerializer(serializers.Serializer):
    session_id = serializers.IntegerField()
    seat_id = serializers.IntegerField()

    class Meta:
        model = Reservation
        fields = "__all__"