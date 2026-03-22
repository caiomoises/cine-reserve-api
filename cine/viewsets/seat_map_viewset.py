from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cine.models.seat import Seat
from cine.models.tickets import Ticket

from core.services.seat_lock import get_seat_lock


class SeatMapViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, session_id):

        seats = Seat.objects.all()  # ou filtrado por sala
        response_data = []

        for seat in seats:

            # 🔒 Verifica se foi comprado
            if Ticket.objects.filter(
                session_id=session_id,
                seat_id=seat.id
            ).exists():
                status = "purchased"

            # 🔒 Verifica Redis
            elif get_seat_lock(session_id, seat.id):
                status = "reserved"

            else:
                status = "available"

            response_data.append({
                "seat_id": seat.id,
                "number": seat.number,
                "status": status
            })

        return Response(response_data)