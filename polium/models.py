import pendulum
from django.db import models
from django.urls import reverse
from util.fields import DateField, DateTimeField
from util.models import HfModel, Survey


# Create your models here.
class Politician(HfModel):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Election(HfModel):
    class ElectionKind(models.TextChoices):
        FEDERAL = "Federal"
        REGIONAL = "Regional (State/Province)"
        MUNICIPAL = "Municipal"

    name = models.CharField(max_length=250)
    date = DateField(default=pendulum.now)
    location = models.CharField(
        max_length=250,
        help_text="Please provide a common/helpful location for this race.",
    )
    kind = models.CharField(choices=ElectionKind.choices, max_length=50)

    def __str__(self):
        return self.name.__str__()

    def get_absolute_url(self):
        return reverse("polium_elections_detail", kwargs={"sqid": self.sqid})


class Candidate(HfModel):
    politician = models.ForeignKey(Politician, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("polium_candidates_detail", kwargs={"sqid": self.sqid})



class PoliticianSurvey(Survey):
    entity = models.ForeignKey(Politician, on_delete=models.CASCADE)
