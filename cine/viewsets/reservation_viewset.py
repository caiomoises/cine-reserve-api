from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cine.models.tickets import Ticket
from cine.models.seat import Seat
from cine.models.session import Session

from cine.serializers.reservation_serializer import ReserveSeatSerializer

from core.services.seat_lock import lock_seat


class ReserveSeatView(APIView):

    def post(self, request):

        serializer = ReserveSeatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        session_id = serializer.validated_data["session_id"]
        seat_id = serializer.validated_data["seat_id"]

        user = request.user

        # 1. Verificar se já foi comprado
        if Ticket.objects.filter(
            session_id=session_id,
            seat_id=seat_id
        ).exists():
            return Response(
                {"error": "Seat already purchased"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 2. Tentar lock no Redis
        locked = lock_seat(
            session_id=session_id,
            seat_id=seat_id,
            user_id=user.id
        )

        if not locked:
            return Response(
                {"error": "Seat already reserved"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # sucesso
        return Response(
            {"message": "Seat reserved successfully"},
            status=status.HTTP_200_OK
        )