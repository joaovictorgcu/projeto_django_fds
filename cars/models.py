from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank = True, null = True)
    model_year = models.IntegerField(blank = True, null = True)
    km = models.IntegerField(blank = True, null = True)
    value = models.FloatField(blank = True, null = True)
    photo = models.ImageField(upload_to='cars/', blank = True, null = True)
    favoritos = models.ManyToManyField(User, related_name='carros_favoritos', blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    

    def __str__(self):
        return self.model


class CarRating(models.Model):
    """Avaliação individual (1 registro por usuário‑carro)."""
    car   = models.ForeignKey(Car, related_name="ratings", on_delete=models.CASCADE)
    user  = models.ForeignKey(User, related_name="car_ratings", on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(6)])  # 0–5
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("car", "user")      # 1 voto por usuário