from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as rest_filters
from rest_framework import filters
from rest_framework.decorators import action


from cars.models import Car
from cars.filters import CarFilter
from cars.serializers import CarSerializer, CarUpdateSerializer, CarCreateSerializer

# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = CarFilter
    search_fields = ['brand','model','vehicle_type']

    def get_serializer_class(self):
        if self.action == "update":
            return CarUpdateSerializer
        elif self.action == "create":
            return CarCreateSerializer
        else:
            return CarSerializer