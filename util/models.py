import pendulum
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_sqids import SqidsField

from util.fields import DateTimeField
from util.storage import gcs


class HfModel(models.Model):
    sqid = SqidsField(real_field_name="id")
    created_at = DateTimeField(default=pendulum.now)

    class Meta:
        abstract = True


class HfUser(AbstractUser):
    sqid = SqidsField(real_field_name="email")


class Activity(HfModel):
    class ActivityKind(models.TextChoices):
        # Polium
        POLIUM_POLITICIAN_SURVEY_COMPLETED = "Politician survey completed"
        POLIUM_REGISTERED_TO_VOTE = "Registered to vote in this race"
        POLIUM_VOLUNTEERED_WITH_CANDIDATE_1H = "Volunteered with the candidate 1 hour"
        POLIUM_VOTED_IN_ELECTION = "Voted in an election"

    kind = models.CharField(choices=ActivityKind.choices, max_length=50)
    points = models.IntegerField(default=0)
    url = models.CharField(max_length=250)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="activities"
    )
    entity = models.IntegerField()
    last_updated_at = DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.sqid} - {self.kind}"

    def as_dict(self):
        return {
            "sqid": self.sqid.str,
            "create_at": self.created_at.to_rfc3339_string(),
            "entity": self.entity.str,
            "kind": self.get_kind_display(),
            "last_updated_at": self.last_updated_at.to_rfc3339_string(),
            "points": self.points,
            "url": self.url,
            "user": str(self.user.sqid),
        }

    def save(self, *args, **kwargs):
        self.last_updated_at = pendulum.now()
        gcs.save_activity(self)
        super().save(*args, **kwargs)


class Category(HfModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Criterion(HfModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.TextField()
    value = models.IntegerField(default=0)

    def __str__(self):
        return (
            f"{self.question[:30]}..."
            if len(str(self.question)) > 40
            else self.question
        )


class Survey(HfModel):
    # TODO: Add an FK to the surveyed record in the app-specific models.py
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    completed_at = DateTimeField(blank=True, null=True)
    expires_at = DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="surveys"
    )
    survey_results = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} -> {self.activity}"

    class Meta:
        abstract = True
