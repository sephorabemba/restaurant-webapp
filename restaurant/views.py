from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from restaurant.models import Booking, Menu
from restaurant.serializers import BookingSerializer, MenuSerializer, UserSerializer
import djoser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.views import LoginView
from django.contrib import messages

template_register = "register.html"
template_login= "login.html"

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello!")

def index(request):
    return render(request, "index.html" , {})

def about(request):
    return render(request, "about.html")

class RegisterUser(APIView):
    def get(self, request):
        # Pass an instance of the serializer to the template context
        serializer = UserSerializer()
        return render(request, template_register, {'serializer': serializer, "request": request})

    def post(self, request):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            # Success message to be displayed on the HTML template
            success_message = f"User {serializer.data['username']} successfully created!"
            # Pass the success message to the template context
            return render(request, template_register, {'serializer': serializer, 'success_message': success_message})
        # If the serializer is not valid, pass it to the template context with errors
        messages.error(request, "Information invalid. Try again.")
        return render(request, template_register, {'serializer': serializer})

class LoginView(LoginView):
    template_name = 'login.html'
    
    def form_invalid(self, form):
        # Add a message to the request object
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#permission_classes = [IsAuthenticated]


#class UserViewSet(djoser.UserViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#permission_classes = [IsAuthenticated]
    
    
# Login user



# Logout user

 
    
class MenuItemView(ListCreateAPIView):
    """
    Methods: GET, POST
    Type: Collection
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    """
    Methods: GET, PUT, PATCH, DELETE
    Type: Single model instance
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


# ----------------------
    
class BookingApiView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True) #do not use data= for GET! You would need to check is_valid() first
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save serialier validated data to the db
            return Response(data={"status": "success", "message": "Booking successfully created.", "data": serializer.data}, status= status.HTTP_201_CREATED )
        else:
            return Response(data={"status": "error", "message": "Can't validate data.", "error": serializer.errors  }, status=status.HTTP_400_BAD_REQUEST)

class MenuApiView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "Menu item successfully created.", "data": serializer.data}, status= status.HTTP_201_CREATED )
        else:
            return Response({"status": "error",  "message": "Can't validate data.",  "error": serializer.errors }, status=status.HTTP_400_BAD_REQUEST)
