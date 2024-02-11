from django.urls import path, include
from restaurant.views import say_hello, index, MenuApiView, BookingApiView, UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework")),
    path("menu", MenuApiView.as_view(), name="menu" ),
    path("booking", BookingApiView.as_view(), name="booking"),
]
