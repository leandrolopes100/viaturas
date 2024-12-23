from django.contrib import admin
from cars.models import Car, Brand #importando a classe 
from cars.models import Batalhao, Situacao


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )

# Só depois de fazer isso que vai mostrar os carros na admin do django
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'situacao',)
    search_fields = ('model', 'brand',)


# e depois temos que registrar para mostrar
admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Batalhao)
admin.site.register(Situacao)
