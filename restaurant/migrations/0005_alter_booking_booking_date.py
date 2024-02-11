# Generated by Django 5.0.2 on 2024-02-11 11:11

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0004_alter_booking_booking_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="booking_date",
            field=models.DateTimeField(
                validators=[
                    django.core.validators.MinValueValidator(
                        django.utils.timezone.now, "You can't book a table in the past."
                    )
                ]
            ),
        ),
    ]
