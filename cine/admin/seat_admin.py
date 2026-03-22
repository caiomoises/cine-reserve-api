from django.contrib import admin
from ..models import Seat

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "row",
        "number",
    )

    search_fields = (
        "session__movie__title",
        "session__room__name",
    )
    ordering = (
        "id",
    )