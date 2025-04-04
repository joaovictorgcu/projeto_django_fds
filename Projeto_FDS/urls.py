from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view,new_car_view
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('carros/', cars_view, name = 'cars_list'),
    path('new_car', new_car_view, name = 'new_car'),
    path('registro/', register_view, name = 'register'),
    path('logout/', logout_view, name = 'logout'),
    path('login', login_view, name = 'login'),
]  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

