from django.db import models

class Room(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    total_rows = models.IntegerField(
        "total_rows",
    )
    
    seats_per_row = models.IntegerField(
        "seats_per_row",
    )

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = "cine"
        verbose_name = "Room"
        verbose_name_plural = "Rooms"