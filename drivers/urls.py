from rest_framework import routers

from drivers import views
from drivers.models import Driver
from drivers.views import DriverViewSet


drivers_router = routers.DefaultRouter()
drivers_router.register(r'drivers_list', views.DriverViewSet, basename=Driver.__name__)
router = routers.DefaultRouter()