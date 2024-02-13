from django import forms
from restaurant.models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["id", "title", "price", "inventory", ]