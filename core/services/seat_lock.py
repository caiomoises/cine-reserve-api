from .redis_client import redis_client


def lock_seat(session_id: int, seat_id: int, user_id: int):
    key = f"seat_lock:{session_id}:{seat_id}"

    created = redis_client.set(
        key,
        user_id,
        nx=True,   # só cria se não existir
        ex=600     # 10 minutos
    )

    if created:
        return True
    else:
        return f'tempo restante: {redis_client.ttl(key)} segundos | tempo restante: {redis_client.ttl(key) // 60} minutos'


def unlock_seat(session_id: int, seat_id: int):
    key = f"seat_lock:{session_id}:{seat_id}"
    redis_client.delete(key)


def is_seat_locked(session_id: int, seat_id: int):
    key = f"seat_lock:{session_id}:{seat_id}"
    return redis_client.exists(key)

def get_seat_lock(session_id: int, seat_id: int):
    key = f"seat_lock:{session_id}:{seat_id}"
    return redis_client.get(key)