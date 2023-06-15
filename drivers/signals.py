from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from  drivers.models import Driver

@receiver(post_save, sender=Driver)
def set_car_status(sender, instance, created, **kwargs):
    if created and instance.rented_car:
        instance.rented_car.is_busy = True
        instance.rented_car.save()


@receiver(pre_delete, sender=Driver)
def unset_car_status(sender, instance, **kwargs):
    if instance.rented_car:
        instance.rented_car.is_busy = False
        instance.rented_car.save()