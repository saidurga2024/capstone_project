from django.urls import path,include
from . import views
from .views import MenuItemView,SingleMenuItemView,BookingViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'booking' ,views.BookingViewSet)


urlpatterns = [
    path('',views.index, name = 'index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('', include(router.urls)),
    path('message/', views.message),
    path('api-token-auth/', obtain_auth_token),
    ]
