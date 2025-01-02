import pendulum
from django.db import models

from util.fields import DateField, DateTimeField
from util.models import HfModel


# Create your models here.
class Politician(HfModel):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Race(HfModel):
    class RaceKind(models.TextChoices):
        FEDERAL = "Federal"
        REGIONAL = "Regional (State/Province)"
        MUNICIPAL = "Municipal"

    name = models.CharField(max_length=250)
    date = DateField(default=pendulum.now)
    location = models.CharField(
        max_length=250,
        help_text="Please provide a common/helpful location for this race.",
    )
    kind = models.CharField(choices=RaceKind.choices, max_length=50)


class Candidate(models.Model):
    created_at = DateTimeField(default=pendulum.now)
    politician = models.ForeignKey(Politician, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
