from rest_framework import serializers

from drivers.models import Driver


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id','username', 'password', 'email', 'first_name', 'last_name', 'birthday', 'address', 'avatar', 'position', 'phone', 'license_category', 'driving_experience']
        extra_kwargs = {'password':{'write_only':True}}


    def create(self, validated_data):
        user = Driver.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birthday=validated_data.get('birthday'),
            address=validated_data.get('address'),
            avatar=validated_data.get('avatar'),
            position=validated_data.get('position'),
            phone=validated_data.get('phone'),
            license_category=validated_data.get('license_category'),
            driving_experience=validated_data.get('driving_experience')
        )
        return user
    