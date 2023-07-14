from rest_framework import viewsets, permissions
from django_filters import rest_framework as rest_filters
from rest_framework import filters
from rest_framework.decorators import action 
from rest_framework.response import Response

from cars.models import Car
from cars.filters import CarFilter
from cars.serializers import CarSerializer, CarUpdateSerializer, CarCreateSerializer
from cars.permissions import IsAdminOrReadOnly
from users.models import User
from users.serializers import UserSerializer

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
        
    @action(methods=["get"], detail=False)
    def top_cars(self, request):
        queryset = self.queryset.filter(top=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
