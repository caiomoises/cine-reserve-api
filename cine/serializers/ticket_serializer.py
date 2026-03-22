from rest_framework import serializers
from cine.models.tickets import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"