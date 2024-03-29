"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from littlelemon import settings
from rest_framework.routers import DefaultRouter
from restaurant import views

router = DefaultRouter()
router.register("api/booking", views.BookingViewSetAPI, basename="reservations-api")
#router.register("restaurant/reservations", views.ReservationsViewSetHTML, basename="reservations")
#router.register("restaurant/booking", views.BookingViewSetHTML, basename="booking")
router.register("restaurant/reservations", views.BookingViewSetAPI, basename="reservations")
router.register("restaurant/booking", views.BookingViewSetAPI, basename="booking")


app_name = "restaurant"

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # presentation
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    # authentication and registration
    path("register/", views.RegisterUser.as_view(), name="register" ),
    path("login/", views.LoginViewHTML.as_view(), name="login-view" ),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout-view'),
    path("auth/", include("djoser.urls"), name="djoser-auth"),
    path("auth/", include("djoser.urls.authtoken")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # menu
    path("", include("restaurant.urls"), name="menu"),
    # booking
    path("", include((router.urls, "restaurant"), namespace="restaurant")),
]
