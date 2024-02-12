from django.urls import path, include
from restaurant import views

urlpatterns = [
    #path("", include(router.urls)),
    path("items", views.MenuItemView.as_view(), name="menu"),
    path("items/<int:pk>", views.SingleMenuItemView.as_view()),
    #path("booking", views.BookingApiView.as_view(), name="booking"),
]
