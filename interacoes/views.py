from interacoes.models import Favorito
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comentario, Mensagem, Conversa, Chat, Message
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cars.models import Car,CarRating, Brand
from django.db.models import Avg, Q
from django.http import JsonResponse
from datetime import datetime

def detalhes_carro(request, carro_id):
    carro = get_object_or_404(Car, id=carro_id)

    ja_favoritado = False
    if request.user.is_authenticated:
        ja_favoritado = Favorito.objects.filter(usuario=request.user, carro=carro).exists()

    return render(request, 'detalhes_carro.html', {
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
    return render(request, 'lista_favoritos.html', {'favoritos': favoritos})

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
    return render(request, 'detalhes_carro.html', context)

@login_required
def editar_carro_view(request, id):
    try:
        car = Car.objects.get(id=id)
    
        if not request.user.is_superuser and car.usuario != request.user:
            return redirect("meus_anuncios") 
        
    except Car.DoesNotExist:
        return redirect("meus_anuncios") 

    if request.method == "POST":
        car.model = request.POST.get("model")
        brand_id = request.POST.get("brand")
        car.brand = Brand.objects.get(id=brand_id)
        car.factory_year = request.POST.get("factory_year")
        car.model_year = request.POST.get("model_year")
        car.km = request.POST.get("km")
        car.value = request.POST.get("value")


        if request.FILES.get("photo"):
            car.photo = request.FILES.get("photo")

        car.save()

        return redirect("meus_anuncios") if not request.user.is_superuser else redirect("todos_anuncios")

    brands = Brand.objects.all()
    return render(request, 'editar_carro.html', {'carro': car, 'brands': brands})


@login_required
def deletar_carro_view(request, id):
    if request.user.is_superuser:
        carro = get_object_or_404(Car, id=id)
    else:
        carro = get_object_or_404(Car, id=id, usuario=request.user)

    carro.delete()
    return redirect("meus_anuncios") if not request.user.is_superuser else redirect("todos_anuncios")

@login_required
def todos_anuncios(request):
    if not request.user.is_superuser:
        return redirect("meus_anuncios")  

    carros = Car.objects.all()
    return render(request, 'todos_anuncios.html', {'carros': carros})

@login_required
def meus_anuncios(request):
    if request.user.is_superuser:
        carros = Car.objects.all()
    else:
        carros = Car.objects.filter(usuario=request.user)

    return render(request, 'meus_anuncios.html', {'carros': carros})

@login_required
def rate_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    try:
        score = int(request.POST.get("score", 0))
        if score not in range(0, 6):
            raise ValueError
    except ValueError:
        messages.error(request, "Nota inválida.")
        return redirect("detalhes_carro", car_id)

    rating, created = CarRating.objects.update_or_create(
        car=car, user=request.user, defaults={"score": score}
    )

    # recalcular média rapidamente
    avg = car.ratings.aggregate(avg=Avg("score"))["avg"] or 0
    car.rating = round(avg, 1)
    car.save(update_fields=["rating"])

    messages.success(request, "Avaliação registrada com sucesso!")
    return redirect("detalhes_carro", car_id)

@login_required
def toggle_favorito(request, car_id):
    carro = get_object_or_404(Car, id=car_id)

    fav, criado = Favorito.objects.get_or_create(
        carro=carro,
        usuario=request.user
    )

    if criado:
        messages.success(request, "Carro adicionado aos favoritos.")
    else:
        fav.delete()
        messages.info(request, "Carro removido dos favoritos.")

    return redirect(request.META.get("HTTP_REFERER", "carros"))

@login_required
def enviar_mensagem(request, carro_id):
    if request.method == 'POST':
        carro = get_object_or_404(Car, id=carro_id)
        conteudo = request.POST.get('conteudo')

        if carro.usuario == request.user:
            return redirect('detalhes_carro', carro_id=carro_id)

        Mensagem.objects.create(
            remetente=request.user,
            destinatario=carro.usuario,
            carro=carro,
            conteudo=conteudo
        )

        return redirect('detalhes_carro', carro_id=carro_id)
    

@login_required
def lista_conversas(request):
    conversas = Conversa.objects.filter(Q(comprador=request.user) | Q(vendedor=request.user)).order_by('-ultima_mensagem')
    
    if not conversas:
        mensagens = 'Você ainda não tem conversas.'
    else:
        mensagens = None
    
    return render(request, 'chat.html', {'conversas': conversas, 'mensagens': mensagens})
@login_required
def iniciar_chat(request, carro_id):
    carro = Car.objects.get(id=carro_id)
    vendedor = carro.usuario

    chat, created = Chat.objects.get_or_create(
        car=carro,
        comprador=request.user,
        vendedor=vendedor
    )

    if created:
        Message.objects.create(
            chat=chat,
            sender=request.user,
            text="Olá, gostaria de saber mais sobre o carro!"
        )

    return redirect('chat_detail', chat_id=chat.id)

@login_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)

    if request.method == 'POST':
        message_text = request.POST.get('message_text') 
        Message.objects.create(
            chat=chat,
            sender=request.user,
            text=message_text
        )
        return redirect('chat_detail', chat_id=chat.id)

    messages = chat.messages.order_by('created_at')

    return render(request, 'chat_detail.html', {'chat': chat, 'messages': messages})
@login_required
def minhas_mensagens(request):
    if request.user.is_superuser:
        chats = Chat.objects.all()
    else:
        chats = Chat.objects.filter(comprador=request.user) | Chat.objects.filter(vendedor=request.user)

    chats_com_mensagens = []
    for chat in chats:
        last_message = chat.messages.order_by('-created_at').first()
        chats_com_mensagens.append({
            'chat': chat,
            'last_message': last_message
        })

    return render(request, 'minhas_mensagens.html', {'chats_com_mensagens': chats_com_mensagens})

@login_required
def excluir_chat(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)

    if request.user == chat.comprador or request.user == chat.vendedor or request.user.is_superuser:
        chat.delete()
        return redirect('minhas_mensagens')
    else:
        return HttpResponseForbidden("Você não tem permissão para excluir este chat.")

@login_required
def todas_mensagens(request):
    if not request.user.is_superuser:
        return redirect('minhas_mensagens')

    chats = Chat.objects.all()
    chats_com_mensagens = []

    for chat in chats:
        ultima_mensagem = chat.messages.last()
        if ultima_mensagem:
            chats_com_mensagens.append({
                'chat': chat,
                'last_message': ultima_mensagem
            })

    return render(request, 'todas_mensagens.html', {'chats_com_mensagens': chats_com_mensagens})


@login_required
def agendar_test_drive(request, carro_id):
    carro = get_object_or_404(Car, id=carro_id)
    vendedor = carro.usuario

    if request.user == vendedor:
        messages.warning(request, "Você não pode agendar um test drive com seu próprio veículo.")
        return redirect('detalhes_carro', carro_id=carro_id)

    if request.method == 'POST':
        data_visita = request.POST.get('data_visita')

        if not data_visita:
            messages.error(request, "Por favor, selecione a data.")
            return redirect('detalhes_carro', carro_id=carro_id)

        # Converte a data para o formato dd-mm-aaaa
        try:
            data_formatada = datetime.strptime(data_visita, "%Y-%m-%d").strftime("%d-%m-%Y")
        except ValueError:
            messages.error(request, "Data inválida.")
            return redirect('detalhes_carro', carro_id=carro_id)

        chat, _ = Chat.objects.get_or_create(
            car=carro,
            comprador=request.user,
            vendedor=vendedor
        )
        Message.objects.create(
            chat=chat,
            sender=request.user,
            text=f"Olá! Agendei um test drive para o dia {data_formatada}."
        )

        messages.success(request, f"Test drive agendado com sucesso para {data_formatada}. O vendedor foi notificado.")
        return redirect('chat_detail', chat_id=chat.id)

    return redirect('detalhes_carro', carro_id=carro_id)