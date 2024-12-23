from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static #importar
from django.conf import settings #importar 
from cars.views import CarsListView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView, CarDashbord
from accounts.views import register_view
from accounts.views import login_view, logout_view

#toda vez que criar uma pagina html tem que ser feito a rota da url aqui
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name ='register'),
    path('login/', login_view, name='login'),
    path('cars/', CarsListView.as_view() , name='cars_list'),
    path('logout/', logout_view, name='logout'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('dashbord/', CarDashbord.as_view(), name='dashbord'),
    path('car_dashboard/csv/', CarDashbord.as_view(), {'action': 'render_csv'}, name='car_dashboard_csv'),  # CSV
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'), 
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'), 
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #tem que fazr isso pra poder utilizar imagens no django
    #int significa que é para pegar o ID do meu objeto (carro), que é um numero inteiro. Ex: Car1, Car2, etc
    #pk é o primary key