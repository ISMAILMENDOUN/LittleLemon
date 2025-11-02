from django.urls import path, include
from . import views
from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'menus', views.Menu)
# router.register(r'bookings', views.Booking)
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItem.as_view()),
]