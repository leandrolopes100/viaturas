from django import forms
from cars.models import Car

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