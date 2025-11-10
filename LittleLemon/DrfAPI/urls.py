from django.urls import path, include, re_path
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
# router.register(r'menus', views.Menu)
router.register(r'bookings', views.BookingViewSet, basename = 'Booking')
router.register(r'menu-items', views.MenuItemViewSet, basename = "menu-item")
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('api-auth-token/', obtain_auth_token),
]