from rest_framework import serializers
from restaurant.models import Menu, Booking
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "groups", ]
        
    def create(self, validated_data):
        # Hash the password before creating the user
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "title", "price", "inventory", ]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

