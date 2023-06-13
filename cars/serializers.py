from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','brand', 'model', 'license_plate', 'vehicle_type', 'image', 'year_production', 'color']

class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'license_plate', 'vehicle_type', 'year_production', 'color']

class CarCreateSerializer(serializers.ModelField):
    class Meta:
        model = Car
        fields = '__all__'


