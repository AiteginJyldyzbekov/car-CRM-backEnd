# Generated by Django 4.2 on 2023-06-14 09:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_rename_image_car_image1_car_image10_car_image2_and_more'),
        ('drivers', '0008_alter_driver_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='cash',
            field=models.IntegerField(default=0, verbose_name='Задолжность'),
        ),
        migrations.AddField(
            model_name='driver',
            name='cash_prove',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография последнего чека'),
        ),
        migrations.AddField(
            model_name='driver',
            name='rented_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cars.car'),
        ),
        migrations.AddField(
            model_name='driver',
            name='rented_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата аренды'),
        ),
        migrations.AddField(
            model_name='driver',
            name='surname',
            field=models.CharField(blank=True, max_length=50, verbose_name='Отчество'),
        ),
    ]