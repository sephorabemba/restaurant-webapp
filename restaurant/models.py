from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.


class Booking(models.Model):
    name = models.CharField(
        max_length=255,
        validators=[
            MinLengthValidator(1, "Your name can't be an empty string."),
        ]
    )
    no_of_guests = models.SmallIntegerField(
        validators=[
            MinValueValidator(0, "You can't invite a negative number of guests."),
            MaxValueValidator(999999, "Number of guests can't exceed 999 999.")
        ]
    )
    booking_date = models.DateTimeField(validators=[MinValueValidator(timezone.now, "You can't book a table in the past.")])
    
    def __str__(self):
        return f"{self.name} - {self.booking_date.strftime('%Y-%m-%d %H:%M:%S')}"
    
class Menu(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(1, "Menu item's name can't be an empty string")])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0, "Menu item's price can't be negative.")])
    inventory = models.SmallIntegerField(
        validators=[
            MinValueValidator(0, "Inventory can't be negative"),
            MaxValueValidator(99999, "Inventory can't exceed 99 999.")
        ]
        
        )
    
    def __str__(self):
        return self.title
