# Generated by Django 5.2.4 on 2025-07-16 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommonField",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("contact", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                (
                    "commonfield_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="app.commonfield",
                    ),
                ),
                ("department", models.CharField(max_length=50)),
            ],
            bases=("app.commonfield",),
        ),
        migrations.CreateModel(
            name="Students",
            fields=[
                (
                    "commonfield_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="app.commonfield",
                    ),
                ),
                ("fees", models.IntegerField()),
            ],
            bases=("app.commonfield",),
        ),
    ]
