from django.test import TestCase
from DrfAPI.views import *



class TestMenuView(TestCase):
    def test_http_methods_status_code(self):
        get_response = self.client.get('/api/menu-items/')
        self.assertEqual(get_response.status_code , 200, "Success")
        post_response = self.client.post('/api/menu-items/', {'title' : "Couscous", 'price' : 50, 'inventory' : 30})
        self.assertEqual(post_response.status_code, 201)
        put_response = self.client.put('/api/menu-items/4/', {'title' : 'Couscous', 'price' : 50, 'inventory' : 40}, content_type = "application/json")
        self.assertEqual(put_response.status_code, 200)
        delete_response = self.client.delete('/api/menu-items/4/')
        self.assertEqual(delete_response.status_code, 204)

class TestBookingView(TestCase):
   def test_http_methods_status_code(self):
        get_response = self.client.get('/api/bookings/')
        self.assertEqual(get_response.status_code , 200, "Success")
        post_response = self.client.post('/api/bookings/', {'name' : "Steve", 'no_of_guests' : 5 , 'booking_date' : "2025-10-05"})
        id = post_response.data['id']
        self.assertEqual(post_response.status_code, 201)
        put_response = self.client.put('/api/bookings/'+str(id)+'/', {'name' : "Steve", 'no_of_guests' : 5 , 'booking_date' : "2025-10-08"}, content_type = "application/json")
        self.assertEqual(put_response.status_code, 200)
        delete_response = self.client.delete('/api/bookings/'+str(id)+'/')
        self.assertEqual(delete_response.status_code, 204)
    

        