from django.contrib import admin
from ..models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "session",
        "seat",
    )

    search_fields = (
        "reservation__user__username",
        "session__movie__title",
        "session__room__name",
        "seat__row",
        "seat__number",
    )
    ordering = (
        "id",
    )