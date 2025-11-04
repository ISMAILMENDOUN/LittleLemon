from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from restaurant.models import Menu, Booking
from .serializers import  MenuItemSerializer, BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .models import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

# class Menu(viewsets.ModelViewSet):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer

# class Booking(viewsets.ModelViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

# class MenuItemView(ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer


# class SingleMenuItem(RetrieveUpdateAPIView, DestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class MenuItemView(ListCreateAPIView):
    permission_classes =[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer 

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

