from rest_framework import serializers
from users.models import User
from cars.models import Car


from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.forms import SetPasswordForm

from django.contrib.auth import authenticate, get_user_model
from djoser.conf import settings
from djoser.serializers import TokenCreateSerializer



User = get_user_model()

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
    


# class PasswordResetSerializer(serializers.Serializer):
#     email = serializers.EmailField()

#     def validate_email(self, value):
#         try:
#             User.objects.get(email=value)
#         except User.DoesNotExist:
#             raise serializers.ValidationError("User with this email does not exist.")
#         return value
    
#     def create(self, validated_data):
#         # Получите пользователя по электронной почте
#         User = get_user_model()
#         user = User.objects.get(email=validated_data['email'])

#         # Создайте и отправьте ссылку для сброса пароля
#         token = default_token_generator.make_token(user)
#         reset_password_url = reverse('password_reset') + f'?uid={user.pk}&token={token}'
#         email_subject = 'Сброс пароля'
#         email_body = f'Для сброса пароля перейдите по ссылке: {reset_password_url}'
#         send_mail(email_subject, email_body, 'from@example.com', [user.email])

#         # Возвращаем что-то, если это необходимо
#         return user

# class PasswordResetConfirmSerializer(serializers.Serializer):
#     uid = serializers.IntegerField()
#     token = serializers.CharField()
#     new_password = serializers.CharField()

#     def validate_uid(self, value):
#         User = get_user_model()
#         try:
#             User.objects.get(pk=value)
#         except User.DoesNotExist:
#             raise serializers.ValidationError(('Недопустимый идентификатор пользователя.'))
#         return value

#     def validate(self, data):
#         uid = data.get('uid')
#         token = data.get('token')
#         new_password = data.get('new_password')

#         User = get_user_model()
#         user = User.objects.get(pk=uid)

#         if not user.is_active:
#             raise serializers.ValidationError(('Пользователь неактивен.'))

#         if not user.check_password(new_password):
#             # Валидация нового пароля с использованием формы SetPasswordForm Django
#             password_validation = SetPasswordForm(user, {'new_password1': new_password})
#             if not password_validation.is_valid():
#                 raise serializers.ValidationError(password_validation.errors)

#         return data


class CustomTokenCreateSerializer(TokenCreateSerializer):

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user: # and self.user.is_active:
            return attrs
        self.fail("invalid_credentials")