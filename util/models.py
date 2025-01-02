from django.contrib.auth.models import AbstractUser

# from django.db import models

# from util.fields import DateTimeField


# Create your models here.
# class HfModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     # created_at = DateTimeField(default=pendulum.now)


class HfUser(AbstractUser):
    pass
