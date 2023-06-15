from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','brand', 'model', 'license_plate', 
                'vehicle_type', 'image1', 'image2', 'image3',
                'image4', 'image5', 'image6', 'passport_image',
                'year_production', 'color', 'last_checking',
                'price_by_day', 'is_busy']

class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'license_plate', 
                'vehicle_type', 'image1', 'image2', 
                'image3', 'image4', 'image5', 'image6',
                'passport_image','year_production', 'color',
                'last_checking', 'price_by_day', 'is_busy']

class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


