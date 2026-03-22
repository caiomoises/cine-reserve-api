from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cine.models.tickets import Ticket
from cine.serializers.ticket_serializer import TicketSerializer


class MyTicketsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tickets = Ticket.objects.filter(user=request.user)
        serializer = TicketSerializer(tickets, many=True)

        return Response(serializer.data)