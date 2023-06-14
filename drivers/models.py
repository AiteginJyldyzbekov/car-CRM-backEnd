from django.db import models
from django.contrib.auth.models import AbstractUser
from cars.models import Car
from django.utils import timezone



class Driver(AbstractUser):
    POSITION_CHOICES = (
        ('ADMIN', 'Администратор'),
        ('MANAGER', 'Менеджер'),
        ('DRIVER', 'Водитель')
    )
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    surname = models.CharField("Отчество", max_length=50, null=True, blank=True)
    birthday = models.DateField("Дата рождения", null=True, blank=True)
    avatar = models.ImageField(upload_to="drivers/avatars", null=True,verbose_name="Фотография водителя")
    position = models.CharField("Позиция пользователя", max_length=20, choices=POSITION_CHOICES, null=True)
    phone = models.CharField("Номер водителя", max_length=50, null=True)
    address = models.CharField("Место проживания", max_length=256, null=True)
    email = models.EmailField("Email", unique=True)
    rented_car = models.OneToOneField(Car,verbose_name='Арендованная машина',on_delete=models.DO_NOTHING,blank=True,null=True)
    rented_date = models.DateField('Дата аренды',default=timezone.now)
    license_category = models.CharField("Категория права", max_length=10, null=True)
    driving_experience = models.CharField("Стаж вождения", max_length=20, null=True)
    cash_verified = models.BooleanField("Верификация оплаты", default=False)
    cash = models.IntegerField('Задолжность',default= 0)
    cash_prove = models.ImageField('Фотография последнего чека',blank=True,null=True)


    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"

    def __str__(self):
        return self.username
    
