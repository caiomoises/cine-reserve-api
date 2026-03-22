from django.contrib import admin
from ..models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "session",
        "status",
    )

    search_fields = (
        "user__username",
        "session__movie__title",
    )
    ordering = (
        "id",
    )