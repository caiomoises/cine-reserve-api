from django.contrib import admin
from ..models import Session

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "movie",
        "room",
        "start_time",
    )

    search_fields = (
        "movie__title",
        "room__name",
    )
    ordering = (
        "id",
    )