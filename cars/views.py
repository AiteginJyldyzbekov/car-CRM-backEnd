from django.shortcuts import render
from rest_framework import viewsets, permissions

from cars.models import Car
from cars.serializers import CarSerializer, CarUpdateSerializer, CarCreateSerializer

# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer(self):
        if self.action == "update":
            return CarUpdateSerializer
        elif self.action == "create":
            return CarCreateSerializer
        else:
            return CarSerializer