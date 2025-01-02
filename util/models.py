import pendulum
from django.contrib.auth.models import AbstractUser

from django.db import models
from django_sqids import SqidsField

from util.fields import DateTimeField


# Create your models here.
class HfModel(models.Model):
    sqid = SqidsField(real_field_name="id")
    created_at = DateTimeField(default=pendulum.now)


class HfUser(AbstractUser):
    sqid = SqidsField(real_field_name="email")
