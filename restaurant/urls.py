from django.urls import path
from restaurant.views import say_hello, index

urlpatterns = [
    path("", index, name="index"),
]
