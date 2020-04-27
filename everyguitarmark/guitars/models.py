from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Guitar(TimeStampedModel):
    class Genre(models.TextChoices):
        GENERIC = "generic", "Generic"
        BLUES = "blues", "Blues"
        SOUL = "soul", "Soul"
        JAZZ = "jazz", "Jazz"
        HARD_ROCK = "hard-rock", "Hard-Rock"
        POP = "pop", "Pop"

    name = models.CharField("Name of Guitar", max_length=255)
    slug = AutoSlugField("Guitar Address",
        unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True)
    genre = models.CharField("Genre", max_length=20,
        choices=Genre.choices, default=Genre.GENERIC)

    def __str__(self):
        return self.name