from django.db import models

# Create your models here.
class Brand(models.Model): #classe criada apenas para 'marca' para ser a foreignkey para usar na classe CAR
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Batalhao(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Situacao(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, null=True, blank=True, verbose_name="Modelo")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand', verbose_name="Marca")
    factory_year = models.IntegerField(blank=True, null=True, verbose_name="Ano de Fabricação")
    model_year = models.IntegerField(blank=True, null=True, verbose_name="Ano do Modelo")
    batalhao = models.ForeignKey(Batalhao, blank=True, null=True, on_delete=models.PROTECT, related_name='cars_batalhao')  # ForeignKey para Batalhao
    prefixo = models.CharField(max_length=10, blank=True, null=True)
    cia = models.CharField(max_length=5, blank=True, null=True)
    pelotao = models.CharField(max_length=5, blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True, verbose_name="Placa")
    value = models.FloatField(blank=True, null=True, verbose_name="Valor FIPE:")
    situacao = models.ForeignKey(Situacao, blank=True, null=True, on_delete=models.PROTECT, related_name='cars_situacao')
    obs = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True, verbose_name="Foto")
    
    def __str__(self):
        return self.model
    
    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return '/path/to/default/image.jpg'  # Caminho para a imagem padrão
    

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
