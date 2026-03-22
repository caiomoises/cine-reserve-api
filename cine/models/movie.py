from django.db import models

class Movie(models.Model):
    title = models.CharField(
        "title",
        max_length=255,
        unique=True,
    )
    
    description = models.TextField(
        "description",
    )
    
    duration = models.IntegerField(
        "duration",
        help_text="Duration in minutes",
    )
    
    release_date = models.DateField(
        "release_date",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        app_label = "cine"
        verbose_name = "Movie"
        verbose_name_plural = "Movies"