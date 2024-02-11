from django.urls import path, include
from restaurant import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("items", views.MenuItemView.as_view(), name="menu"),
    path("items/<int:pk>", views.SingleMenuItemView.as_view()),
    #path("booking", views.BookingApiView.as_view(), name="booking"),
]
