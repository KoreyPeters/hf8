# Generated by Django 5.1.4 on 2025-01-06 02:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polium", "0004_rename_politiciansurvey_candidatesurvey"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="candidatesurvey",
            unique_together={("entity", "user")},
        ),
    ]
