from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
# router.register(r'menus', views.Menu)
router.register(r'bookings', views.BookingViewSet, basename = 'Booking')
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
    # path('menu/', views.MenuItemView.as_view()),
    # path('menu/<int:pk>', views.SingleMenuItem.as_view()),
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]