from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as rest_filters
from rest_framework import filters
from rest_framework.decorators import action 

from rest_framework import viewsets, permissions
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from drivers.models import Driver
from drivers.serializers import DriverSerializer
from drivers.filters import DriverFilter

class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    permission_classes = [permissions.AllowAny]
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = DriverFilter
    search_fields = ['first_name','last_name','rented_date']


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        refresh = RefreshToken.for_user(serializer.instance)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
    
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Неверные учетные данные.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    @action(methods=["get"], detail=False)
    def verified(self, request):
        queryset = self.queryset.filter(cash_verified=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

