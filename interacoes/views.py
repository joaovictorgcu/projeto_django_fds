from django.shortcuts import redirect, get_object_or_404
from interacoes.models import Favorito
from cars.models import Car
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comentario

def detalhes_carro(request, carro_id):
    carro = get_object_or_404(Car, id=carro_id)

    ja_favoritado = False
    if request.user.is_authenticated:
        ja_favoritado = Favorito.objects.filter(usuario=request.user, carro=carro).exists()

    return render(request, 'interacoes/detalhes_carro.html', {
        'carro': carro,
        'ja_favoritado': ja_favoritado
    })


@login_required
def favoritar_carro(request, carro_id):
    carro = get_object_or_404(Car, id=carro_id)
    favorito_existente = Favorito.objects.filter(usuario=request.user, carro=carro).first()
    if not favorito_existente:
        Favorito.objects.create(usuario=request.user, carro=carro)

    return redirect('detalhes_carro', carro_id=carro.id)

@login_required
def lista_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user)
    return render(request, 'interacoes/lista_favoritos.html', {'favoritos': favoritos})



from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Comentario
from cars.models import Car  # certifique-se que está importando o modelo certo

def detalhes_carro(request, carro_id):
    carro = get_object_or_404(Car, id=carro_id)

    ja_favoritado = False
    if request.user.is_authenticated:
        ja_favoritado = Favorito.objects.filter(usuario=request.user, carro=carro).exists()

    comentarios = Comentario.objects.filter(carro=carro).order_by('-criado_em')

    if request.method == "POST" and request.user.is_authenticated:
        texto = request.POST.get('texto')
        if texto:
            comentario = Comentario.objects.create(
                carro=carro,
                autor=request.user,
                texto=texto,
            )
            return JsonResponse({
                'autor': comentario.autor.username,
                'texto': comentario.texto,
                'data': comentario.criado_em.strftime('%d/%m/%Y %H:%M')
            })

    context = {
        'carro': carro,
        'ja_favoritado': ja_favoritado,
        'comentarios': comentarios,
    }
    return render(request, 'interacoes/detalhes_carro.html', context)

@login_required
def editar_carro_view(request, id):
    carro = Car.objects.get(id=id, user=request.user)

    if request.method == "POST":
        carro.model = request.POST.get("model")
        brand_id = request.POST.get("brand")
        carro.brand = Brand.objects.get(id=brand_id)
        carro.factory_year = request.POST.get("factory_year")
        carro.model_year = request.POST.get("model_year")
        carro.km = request.POST.get("km")
        carro.value = request.POST.get("value")
        
        if request.FILES.get("photo"):
            carro.photo = request.FILES.get("photo")

        carro.save()
        return redirect("meus_anuncios")

    brands = Brand.objects.all()
    return render(request, 'editar_carro.html', {'carro': carro, 'brands': brands})

@login_required
def deletar_carro_view(request, id):
    carro = Car.objects.get(id=id, usuario=request.user)
    carro.delete()
    return redirect("meus_anuncios")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cars.models import Car

@login_required
def meus_anuncios(request):
    carros = Car.objects.filter(usuario=request.user) 
    return render(request, 'meus_anuncios.html', {'carros': carros})
