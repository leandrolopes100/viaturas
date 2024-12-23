from django import forms
from cars.models import Brand, Car
#essa pagina é para criar todos os formulários
#criado para fazer com que o usuario insere novos carros direto pela pagina html

#classe com os mesmos objetos do models.py
#isso é criado depois da pagina new_car.html
# class CarForm(forms.Form): #maneira manual de criar o formulário para o usuário
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all()) #importando a chave estrangeira da tabela de marcas
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     photo = forms.ImageField()
    
#     def save(self): #funcao para criar um novo carro SELF é para acessar o formulario
#         car = Car( #instaciando um objeto do banco de dados "CAR", com os dados do form
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             factory_year = self.cleaned_data['factory_year'],
#             model_year = self.cleaned_data['model_year'],
#             plate = self.cleaned_data['plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],
#         )
#         car.save() #para salvar o objeto na tabel(model)
#         return car
    

    #isso tem que fazer para salvar o formulário no models
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car #qual modelo? = lá do Car
        fields = '__all__' #quais campos do modelo Car? = Todos

    def clean_value(self): #validando o campo value
        value = self.cleaned_data.get('value')
        if value is None:
            self.add_error('value', 'Valor mínimo da viatura deve ser de R$20.000')
        else:
            return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1700 or factory_year is None:
              self.add_error('factory_year', 'Insira um carro com o ano de fabricação maior que 1980')
        else:
            return factory_year