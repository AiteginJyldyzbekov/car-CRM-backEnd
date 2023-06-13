from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Driver(AbstractUser):
    POSITION_CHOICES = (
        ('ADMIN', 'Администратор'),
        ('MANAGER', 'Менеджер'),
        ('DRIVER', 'Водитель')
    )
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    birthday = models.DateField("Дата рождения", null=True, blank=True)
    avatar = models.ImageField(upload_to="drivers/avatars", null=True,verbose_name="Фотография водителя")
    position = models.CharField("Позиция пользователя", max_length=20, choices=POSITION_CHOICES, null=True)
    phone = models.CharField("Номер водителя", max_length=50, null=True)
    address = models.CharField("Место проживания", max_length=256, null=True)
    email = models.EmailField("Email", unique=True)
    license_category = models.CharField("Категория права", max_length=10, null=True)
    driving_experience = models.CharField("Стаж вождения", max_length=20, null=True)


    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"

    def __str__(self):
        return self.username
    
