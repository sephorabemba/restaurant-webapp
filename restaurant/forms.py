from django import forms
from restaurant.models import Menu, Booking
from django.forms.widgets import DateInput, DateTimeInput

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["id", "title", "price", "inventory", ]
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["id", "name", "no_of_guests", "booking_date", ]
        widgets = {
            'booking_date': DateInput(attrs={'type': 'datetime-local'}),
        }
