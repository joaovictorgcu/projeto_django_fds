from django.urls import path
from . import views
from cars.views import index_view, cars_view, new_car_view, meus_anuncios
from .views import editar_carro_view, deletar_carro_view
from django.conf import settings
from django.conf.urls.static import static
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
    path("toggle-favorito/<int:car_id>/", views.toggle_favorito, name="toggle_favorito"),
    path("rate-car/<int:car_id>/", views.rate_car, name="rate_car"),
    path('carro/<int:carro_id>/enviar_mensagem/', views.enviar_mensagem, name='enviar_mensagem'),
    path("mensagens/", views.minhas_mensagens, name="minhas_mensagens"),
    path("mensagem/enviar/<int:carro_id>/", views.enviar_mensagem, name="enviar_mensagem"),
    path('chat/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('iniciar-chat/<int:carro_id>/', views.iniciar_chat, name='iniciar_chat'),
    path('todos-anuncios/', views.todos_anuncios, name='todos_anuncios'),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
