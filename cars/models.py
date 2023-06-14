from django.db import models


from django.core.validators import MaxValueValidator

# Create your models here.

class Car(models.Model):
    brand = models.CharField("Марка автомобиля", max_length=50)
    model = models.CharField("Модель автомобиля", max_length=50)
    license_plate = models.CharField("Государственный номер автомобиля", max_length=10, null=True, blank=True)
    vehicle_type = models.CharField("Тип кузова", max_length=20)
    image1 = models.ImageField("Фотография автомобиля", upload_to="cars/images", null=True,blank=True)
    year_production = models.IntegerField("Год выпуска", null=True, validators=[MaxValueValidator(2050)])
    color = models.CharField("Цвет", max_length=20, null=True)


    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return self.brand
    