# Generated by Django 5.1.4 on 2025-01-02 04:32

import django.db.models.deletion
import pendulum
import util.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Politician",
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
                ("first_name", models.CharField(max_length=250)),
                ("last_name", models.CharField(max_length=250)),
                ("rating", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Race",
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
                ("name", models.CharField(max_length=250)),
                ("date", util.fields.DateField(default=pendulum.now)),
                (
                    "location",
                    models.CharField(
                        help_text="Please provide a common/helpful location for this race.",
                        max_length=250,
                    ),
                ),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("Federal", "Federal"),
                            ("Regional (State/Province)", "Regional"),
                            ("Municipal", "Municipal"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Candidate",
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
                (
                    "politician",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="polium.politician",
                    ),
                ),
                (
                    "race",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polium.race"
                    ),
                ),
            ],
        ),
    ]
