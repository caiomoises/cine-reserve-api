from cine.models.tickets import Ticket
from cine.models.session import Session
from cine.models.seat import Seat

from core.services.seat_lock import get_seat_lock, unlock_seat


def process_checkout(user, session_id, seat_id):
    # Verifica se já foi comprado
    if Ticket.objects.filter(session_id=session_id, seat_id=seat_id).exists():
        raise Exception("Seat already purchased")

    # Verifica lock
    lock_owner = get_seat_lock(session_id, seat_id)

    if not lock_owner:
        raise Exception("Seat is not reserved")

    if str(lock_owner) != str(user.id):
        raise Exception("Seat reserved by another user")

    # Criar ticket
    ticket = Ticket.objects.create(
        user=user,
        session_id=session_id,
        seat_id=seat_id
    )

    # Remove lock
    unlock_seat(session_id, seat_id)

    return ticket