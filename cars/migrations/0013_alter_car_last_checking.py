# Generated by Django 4.2 on 2023-06-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_alter_car_passport_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='last_checking',
            field=models.DateField(null=True, verbose_name='Последний технический осмотр'),
        ),
    ]
