from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from restaurant.models import Booking, Menu
from restaurant.serializers import BookingSerializer, MenuSerializer, UserSerializer

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello!")

def index(request):
    return render(request, "index.html" , {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    

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
