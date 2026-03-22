from django.db import models
import uuid

class Ticket(models.Model):
    user = models.ForeignKey(
        "cine.User",
        on_delete=models.CASCADE
    )

    session = models.ForeignKey(
        "cine.Session",
        on_delete=models.CASCADE
    )

    seat = models.ForeignKey(
        "cine.Seat",
        on_delete=models.CASCADE
    )

    code = models.UUIDField(
        default=uuid.uuid4,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Ticket {self.code} for {self.session} - Seat {self.seat}"
    
    class Meta:
        app_label = "cine"
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        unique_together = ("session", "seat")