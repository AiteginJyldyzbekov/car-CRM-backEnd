# Generated by Django 4.2 on 2023-06-14 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0012_driver_cash_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='surname',
            field=models.CharField(max_length=50, verbose_name='Отчество'),
        ),
    ]