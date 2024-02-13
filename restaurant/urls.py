from django.urls import path
from restaurant import views
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("auth/api-token-auth", obtain_auth_token),
    path("api/menu/items", views.MenuItemViewAPI.as_view(), name="menu-items-api"),
    path("restaurant/menu/items", login_required(views.MenuItemViewHTML.as_view()), name="menu-items"),
    path("api/menu/items/<int:pk>", views.SingleMenuItemViewAPI.as_view(), name="menu-item-api"),
    path("restaurant/menu/items/<int:pk>", login_required(views.SingleMenuItemViewHTML.as_view()), name="menu-item"),
]
