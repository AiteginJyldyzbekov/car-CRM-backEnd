from django.db import models


from django.core.validators import MaxValueValidator


# Create your models here.

class Car(models.Model):
    brand = models.CharField("Марка автомобиля", max_length=50)
    model = models.CharField("Модель автомобиля", max_length=50)
    license_plate = models.CharField("Государственный номер автомобиля", max_length=10, null=True)
    vehicle_type = models.CharField("Тип кузова", max_length=20)
    image1 = models.ImageField("Фотография автомобиля с правой стороны", upload_to="cars/images", null=True)
    image2 = models.ImageField("Фотография автомобиля с левой стороны", upload_to="cars/images", null=True)
    image3 = models.ImageField("Фотография автомобиля с задней стороны", upload_to="cars/images", null=True)
    image4 = models.ImageField("Фотография автомобиля с передней стороны", upload_to="cars/images", null=True)
    image5 = models.ImageField("Фотография автомобиля изнутри(необязательно)", upload_to="cars/images",blank=True)
    image6 = models.ImageField("Фотография автомобиля изнутри(необязательно)", upload_to="cars/images",blank=True)
    passport_image = models.ImageField("Фотография Техпаспорта", upload_to="cars/passport_images", null=True)
    year_production = models.IntegerField("Год выпуска", null=True, validators=[MaxValueValidator(2050)])
    color = models.CharField("Цвет", max_length=20, null=True)
    last_checking = models.DateField("Последний технический осмотр", null=True)
    price_by_day = models.CharField("Цена по суточной оплаты", max_length=20, null=True)
    is_busy = models.BooleanField(default=False)
    top = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        full_name = f"{self.brand} {self.model} {self.license_plate}"
        return full_name
    