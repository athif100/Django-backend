# Generated by Django 5.1.2 on 2024-10-19 05:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aniapp", "0002_alter_artical_created"),
    ]

    operations = [
        migrations.CreateModel(
            name="Characters",
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
                ("first_name", models.CharField(max_length=60)),
                ("second_name", models.CharField(max_length=60)),
                ("image", models.ImageField(upload_to="")),
                ("discription", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Technique",
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
                ("red_name", models.CharField(max_length=60)),
                ("damage_amount", models.IntegerField()),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="aniapp.characters",
                    ),
                ),
            ],
        ),
    ]