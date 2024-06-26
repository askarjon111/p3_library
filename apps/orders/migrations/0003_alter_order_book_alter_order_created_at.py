# Generated by Django 5.0.4 on 2024-05-02 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_rename_genre_book_genres"),
        ("orders", "0002_order_book"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="book",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="books.book",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(auto_created=True, auto_now_add=True),
        ),
    ]
