from django.db import models

class Seat(models.Model):
    room = models.ForeignKey(
        "cine.Room",
        on_delete=models.CASCADE
    )

    row = models.CharField(
        max_length=2
    )

    number = models.IntegerField()

    def __str__(self):
        return f"Seat {self.row}{self.number} in {self.room.name}"

    class Meta:
        app_label = "cine"
        verbose_name = "Seat"
        verbose_name_plural = "Seats"
        unique_together = ("room", "row", "number")