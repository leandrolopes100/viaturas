from django.urls import reverse_lazy, reverse
import csv
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cars.models import Car, Batalhao
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.db.models import Q
from django.http import HttpResponse


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('batalhao')
        search = self.request.GET.get('search')
        batalhao = self.request.GET.get('batalhao')
     
        if search:
            cars = cars.filter(
                Q(model__icontains=search) |
                Q(plate__contains=search) |
                Q(prefixo__contains=search)
            )
        
        if batalhao:
            cars = cars.filter(batalhao_id=batalhao)
        return cars
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['batalhoes'] = Batalhao.objects.all()
        cars = self.get_queryset()  # Atualizando a lista de carros com base no queryset filtrado
        context['cars'] = cars  # Passando a lista de carros para o template
        context['qap_count'] = cars.filter(situacao__name="QAP").count()
        context['fa_count'] = cars.filter(situacao__name="F.A").count()
        context['manutencao_count'] = cars.filter(situacao__name="Manutenção").count()

        return context

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        cars = list(Car.objects.order_by('pk'))
        car_index = cars.index(car)

        prev_car = cars[car_index - 1] if car_index > 0 else None
        next_car = cars[car_index + 1] if car_index < len(cars) - 1 else None

        context['prev_car'] = prev_car
        context['next_car'] = next_car
        return context

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDashbord(TemplateView):
    model = Car
    template_name = 'car_dashbord.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obter todos os carros e ordenar por batalhao
        cars = Car.objects.all().order_by('batalhao')
        
        # Contagem das situações das viaturas
        context['qap_count'] = cars.filter(situacao__name="QAP").count()
        context['fa_count'] = cars.filter(situacao__name="F.A").count()
        context['manutencao_count'] = cars.filter(situacao__name="Manutenção").count()
        context['total_viaturas'] = cars.count()
        
        # Passar a lista de carros para o template
        context['cars'] = cars
        
        # URL para o download do CSV
        context['csv_download_url'] = reverse('car_dashboard_csv')
        
        return context

    def render_csv(self, request, *args, **kwargs):
        # Criar uma resposta HTTP com o tipo de conteúdo para CSV
        response = HttpResponse(content_type='text/csv', charset='utf-8')
        response['Content-Disposition'] = 'attachment; filename="relatorio_viaturas.csv"'
        response['Content-Encoding'] = 'utf-8'
        
        # Criar o escritor de CSV
        writer = csv.writer(response, delimiter=';', lineterminator='\r\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # Escrever os cabeçalhos
        writer.writerow(['Modelo', 'Batalhão', 'Pelotão', 'Cia', 'Situação', 'Prefixo'])
        
        # Escrever os dados das viaturas
        cars = Car.objects.all().order_by('batalhao')
        for car in cars:
                writer.writerow([f"{car.brand.name} {car.model}", car.batalhao, car.pelotao, car.cia, car.situacao, car.prefixo])
        return response
    
    def dispatch(self, request, *args, **kwargs):
        action = kwargs.get('action')
        if action == 'render_csv':
            return self.render_csv(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)
    

