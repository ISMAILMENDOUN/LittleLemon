from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from restaurant.models import Menu, Booking
from .serializers import  MenuItemSerializer, BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from restaurant.models import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class MenuItemViewSet(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer 

