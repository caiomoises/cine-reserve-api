from django.db import models

class Reservation(models.Model):

    STATUS = [
        ("locked", "Locked"),
        ("purchased", "Purchased"),
    ]

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

    status = models.CharField(
        max_length=20, 
        choices=STATUS
    )

    expires_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Reservation for {self.session} - Seat {self.seat} by {self.user.username} ({self.status})"
    
    class Meta:
        app_label = "cine"
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
        unique_together = ("session", "seat")