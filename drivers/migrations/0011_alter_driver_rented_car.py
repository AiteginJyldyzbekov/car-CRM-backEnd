# Generated by Django 4.2 on 2023-06-14 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_remove_car_image10_remove_car_image2_and_more'),
        ('drivers', '0010_alter_driver_rented_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='rented_car',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cars.car', verbose_name='Арендованная машина'),
        ),
    ]
