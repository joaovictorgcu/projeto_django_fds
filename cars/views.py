from django.shortcuts import render, redirect
from cars.models import Car, Brand

def cars_view(request): 
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    
    if search:
        cars = cars.filter(model__icontains = search).order_by('model')

    return render(
        request, 
        'cars.html',
        {'cars': cars}
    )

def new_car_view(request):
    if request.method == "POST":
        model = request.POST.get("model")
        brand_id = request.POST.get("brand")
        factory_year = request.POST.get("factory_year")
        model_year = request.POST.get("model_year")
        km = request.POST.get("km")
        value = request.POST.get("value")
        photo = request.FILES.get("photo")

        brand = Brand.objects.get(id=brand_id)

        Car.objects.create(
            model=model,
            brand=brand,
            factory_year=factory_year,
            model_year=model_year,
            km=km,
            value=value,
            photo=photo
        )

        return redirect("cars_list")
    
    brands = Brand.objects.all()
    return render(request, 'new_car.html', {'brands': brands})


def index_view(request):
    return render(request, 'index.html')



