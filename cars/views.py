from django.shortcuts import render, redirect
from cars.models import Car, Brand
from interacoes.models import Favorito
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def cars_view(request): 
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    
    if search:
        cars = cars.filter(model__icontains=search)

    favoritos_ids = []
    if request.user.is_authenticated:
        favoritos_ids = list(
            Favorito.objects.filter(usuario=request.user).values_list('carro_id', flat=True)
        )

    return render(
        request, 
        'cars.html',
        {'cars': cars.order_by('model'), 'favoritos_ids': favoritos_ids}
    )

@login_required
def new_car_view(request):
    if request.method == "POST":
        model = request.POST.get("model")
        brand_id = request.POST.get("brand")
        factory_year = request.POST.get("factory_year")
        model_year = request.POST.get("model_year")
        km = request.POST.get("km")
        value = request.POST.get("value")
        photo = request.FILES.get("photo")

        if not all([model, brand_id, factory_year, model_year, km, value, photo]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect("new_car")

        try:
            brand = Brand.objects.get(id=brand_id)
        except Brand.DoesNotExist:
            messages.error(request, "Marca inválida.")
            return redirect("new_car")

        Car.objects.create(
            model=model,
            brand=brand,
            factory_year=factory_year,
            model_year=model_year,
            km=km,
            value=value,
            photo=photo,
            usuario=request.user  # <-- campo correto!
        )

        messages.success(request, "Carro cadastrado com sucesso!")
        return redirect("cars_list")
    
    brands = Brand.objects.all()
    return render(request, 'new_car.html', {'brands': brands})

def index_view(request):
    return render(request, 'index.html')

@login_required
def meus_anuncios(request):
    carros = Car.objects.filter(usuario=request.user).order_by('-factory_year', '-model_year')  # <-- campo correto!
    return render(request, 'meus_anuncios.html', {'carros': carros})
