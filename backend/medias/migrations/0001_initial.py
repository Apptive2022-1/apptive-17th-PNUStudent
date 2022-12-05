# Generated by Django 4.1.3 on 2022-11-27 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("announces", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("file", models.URLField()),
                ("description", models.CharField(max_length=140)),
                (
                    "announce",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="announces.announce",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]