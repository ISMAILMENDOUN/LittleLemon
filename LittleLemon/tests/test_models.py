from django.test import TestCase
from restaurant.models import *
from DrfAPI.serializers import MenuItemSerializer
from datetime import date
class TestMenuModel(TestCase):
    def setUp(self):
        Menu.objects.create(title = "Item1", price = 20 , inventory = 10)
        Menu.objects.create(title = "Item2", price = 20 , inventory = 20)
        Menu.objects.create(title = "Item3", price = 20 , inventory = 10)
    
    def test_response(self):
        response = self.client.get('/api/menu-items/1/')
        self.assertEqual(response.data['title'], "Item1")
    
class TestBookingModel(TestCase):
    def setUp(self):
        Booking.objects.create(name = "Steve", no_of_guests = 5 , booking_date = "2025-10-05" )
    def test_response(self):
        response = self.client.get('/api/bookings/1/')
        self.assertEqual(response.data, {'id' : 1, 'name' : 'Steve', 'no_of_guests' : 5 , 'booking_date' : '2025-10-05T00:00:00Z'})
