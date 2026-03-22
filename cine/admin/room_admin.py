from django.contrib import admin
from ..models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "total_rows",
        "seats_per_row"
    )

    search_fields = (
        "name",
    )
    ordering = (
        "id",
    )