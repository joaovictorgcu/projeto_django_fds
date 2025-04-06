from django.urls import path
from . import views

urlpatterns = [
    path('carro/<int:carro_id>/', views.detalhes_carro, name='detalhes_carro'),
    path('carro/<int:carro_id>/favoritar/', views.favoritar_carro, name='favoritar_carro'),
    path('favoritos/', views.lista_favoritos, name='lista_favoritos'), 
]
