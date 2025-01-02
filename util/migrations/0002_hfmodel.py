# Generated by Django 5.1.4 on 2025-01-02 04:15

import pendulum
import util.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("util", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HfModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", util.fields.DateTimeField(default=pendulum.now)),
            ],
        ),
    ]
