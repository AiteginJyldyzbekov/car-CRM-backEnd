from rest_framework import routers

from cars import views
from cars.models import Car
from cars.views import CarViewSet


cars_router = routers.DefaultRouter()
cars_router.register(r'cars_list', views.CarViewSet, basename=Car.__name__)
router = routers.DefaultRouter()