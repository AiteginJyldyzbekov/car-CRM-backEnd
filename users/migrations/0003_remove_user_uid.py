# Generated by Django 4.2 on 2023-07-01 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uid',
        ),
    ]