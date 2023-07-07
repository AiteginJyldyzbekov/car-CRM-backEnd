from rest_framework import viewsets, permissions
from django_filters import rest_framework as rest_filters
from rest_framework import filters

from cars.models import Car
from cars.filters import CarFilter
from cars.serializers import CarSerializer, CarUpdateSerializer, CarCreateSerializer
from cars.permissions import IsAdminOrReadOnly

# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = CarFilter
    search_fields = ['brand','model','vehicle_type','license_plate']

    def get_serializer_class(self):
        if self.action == "update":
            return CarUpdateSerializer
        elif self.action == "create":
            return CarCreateSerializer
        else:
            return CarSerializer