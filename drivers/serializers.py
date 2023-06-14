from rest_framework import serializers

from drivers.models import Driver
from cars.serializers import CarSerializer


class DriverSerializer(serializers.ModelSerializer):
    rented_car = serializers.SerializerMethodField()
    class Meta:
        model = Driver
        fields = ['id','username','password','first_name', 'last_name', 
                  'surname', 'birthday', 'avatar', 'position', 
                  'phone','address', 'email', 'rented_car',
                  'rented_date','license_category','driving_experience', 
                  'cash_verified', 'cash','cash_prove' ]
        extra_kwargs = {'password':{'write_only':True}}

    def get_rented_car(self, instance):
        rented_car = instance.rented_car
        if rented_car:
            return {
                'id': rented_car.id,
                'brand': rented_car.brand,
                'model': rented_car.model,
                'license_plate': rented_car.license_plate,
                'color': rented_car.color
            }
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        rented_car_data = self.get_rented_car(instance)
        representation['rented_car'] = rented_car_data
        return representation
    

    def create(self, validated_data):
        user = Driver.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            surname=validated_data.get('surname'),
            birthday=validated_data.get('birthday'),
            avatar=validated_data.get('avatar'),
            position=validated_data.get('position'),
            phone=validated_data.get('phone'),
            address=validated_data.get('address'),
            email=validated_data['email'],
            rented_car=validated_data.get('rented_car'),
            rented_date=validated_data.get('rented_date'),
            license_category=validated_data.get('license_category'),
            driving_experience=validated_data.get('driving_experience'),
            cash_verified=validated_data.get('cash_verified'),
            cash=validated_data.get('cash'),
            cash_prove=validated_data.get('cash_prove')
        )
        return user

