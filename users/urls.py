from rest_framework import routers

from users import views
from users.models import User
from users.views import UserViewSet


users_router = routers.DefaultRouter()
users_router.register(r'users_list', views.UserViewSet, basename=User.__name__)
router = routers.DefaultRouter()