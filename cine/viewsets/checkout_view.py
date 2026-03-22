from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from cine.serializers.checkout_serializer import CheckoutSerializer
from core.services.checkout_service import process_checkout


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CheckoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            ticket = process_checkout(
                user=request.user,
                session_id=serializer.validated_data["session_id"],
                seat_id=serializer.validated_data["seat_id"],
            )

            return Response({
                "message": "Ticket purchased successfully",
                "ticket_id": ticket.id
            })

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )