import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Pet(models.Model):
    """Represents an animal pet."""

    SPECIES_CHOICES = [
        ("cat", "Cat"),
        ("dog", "Dog"),
        ("hamster", "Hamster"),
    ]

    name = models.CharField(max_length=50)
    species = models.CharField(choices=SPECIES_CHOICES, max_length=10)
    year_of_birth = models.IntegerField(
        validators=[
            MinValueValidator(
                1950, message="Year of birth must be before 1950"
            ),
            MaxValueValidator(
                datetime.date.today().year,
                message="Year of birth can't be in the future",
            ),
        ]
    )

    def __str__(self):
        """Human representable pet name."""
        return f"{self.name} ({self.species})"

    def get_absolute_url(self):
        """Redirect to the pet lists page after creation."""
        from django.urls import reverse

        return reverse("pets")
