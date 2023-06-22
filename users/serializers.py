from rest_framework import serializers


from users.models import User
from cars.models import Car


class UserSerializer(serializers.ModelSerializer):
    rented_car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), allow_null=True)
    class Meta:
        model = User
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
        user = User.objects.create_user(
            username=validated_data['username'],
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
        password = validated_data['password']
        user.set_password(password)  # Захешировать пароль
        user.save()
        return user

