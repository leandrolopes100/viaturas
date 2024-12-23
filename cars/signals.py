from django.db.models import post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory


def car_invetory_update(): #função para atualizar o estoque 
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value'] 
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)
    
@receiver(post_save, sender=Car)
def car_post_save(sender, instanse, **kwargs):
   car_invetory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instanse, **kwargs):
    car_invetory_update()
