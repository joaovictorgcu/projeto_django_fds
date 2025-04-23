from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from cars.views import cars_view, new_car_view, index_view
from accounts.views import register_view, login_view, logout_view
from interacoes.views import meus_anuncios
from MATCHAUTOS import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('index', permanent=False)),
    path('carros/', cars_view, name='cars_list'),
    path('new_car', new_car_view, name='new_car'),
    path('registro/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('index/', index_view, name='index'),
    path('interacoes/', include('interacoes.urls')),
    path('meus-anuncios/', meus_anuncios, name='meus_anuncios'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
