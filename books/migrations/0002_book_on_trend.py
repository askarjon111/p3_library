# Generated by Django 5.0.4 on 2024-04-30 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="on_trend",
            field=models.BooleanField(default=False),
        ),
    ]
