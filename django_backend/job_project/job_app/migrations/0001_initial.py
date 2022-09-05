# Generated by Django 4.1 on 2022-09-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Application",
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
                ("candidate", models.CharField(blank=True, max_length=100)),
                ("job_type", models.CharField(blank=True, max_length=50)),
                ("status", models.CharField(default="Applied", max_length=50)),
                ("message", models.CharField(blank=True, max_length=2000)),
                ("contact", models.IntegerField(blank=True)),
                ("email", models.EmailField(blank=True, max_length=254, unique=True)),
                ("skills", models.CharField(blank=True, max_length=255)),
                ("resume", models.FileField(blank=True, upload_to="")),
                ("address", models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]