from django.urls import path
from . import views
from cars.views import index_view, cars_view, new_car_view, meus_anuncios
from .views import editar_carro_view, deletar_carro_view


urlpatterns = [
    path('carro/<int:carro_id>/', views.detalhes_carro, name='detalhes_carro'),
    path('carro/<int:carro_id>/favoritar/', views.favoritar_carro, name='favoritar_carro'),
    path('favoritos/', views.lista_favoritos, name='lista_favoritos'), 
    path('', index_view, name='index'),
    path('carros/', cars_view, name='cars_list'),
    path('novo-carro/', new_car_view, name='new_car'),
    path('meus-anuncios/', meus_anuncios, name='meus_anuncios'),
    path('editar-carro/<int:id>/', editar_carro_view, name='editar_carro'),
    path('deletar-carro/<int:id>/', deletar_carro_view, name='deletar_carro'),
]

