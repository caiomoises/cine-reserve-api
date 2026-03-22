from django.db import models
from .room import Room

class Session(models.Model):
    movie = models.ForeignKey(
        "cine.Movie",
        on_delete=models.CASCADE
    )

    room = models.ForeignKey(
        "cine.Room",
        on_delete=models.CASCADE
    )

    start_time = models.DateTimeField(
        "start_time",
    )

    def __str__(self):
        return f"{self.movie.title} at {self.start_time} in {self.room.name}"
    
    class Meta:
        app_label = "cine"
        verbose_name = "Session"
        verbose_name_plural = "Sessions"