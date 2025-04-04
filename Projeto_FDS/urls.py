from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('carros/', cars_view),
]   + static(settings.MEDIA_URL, documento_root = settings.MEDIA_ROOT)

