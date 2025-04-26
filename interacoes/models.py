from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carro = models.ForeignKey(Car, on_delete=models.CASCADE)
    data_favorito = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} favoritou {self.carro}"

class Comentario(models.Model):
    carro = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.autor.username} em {self.carro.model}'



class Conversa(models.Model):
    carro = models.ForeignKey(Car, on_delete=models.CASCADE)
    comprador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comprador_conversas')
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendedor_conversas')
    ultima_mensagem = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comprador.username} - {self.carro.model}"

class Mensagem(models.Model):
    conversa = models.ForeignKey(Conversa, on_delete=models.CASCADE, null=True, blank=True)  # Permite valor nulo
    remetente = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.remetente.username} em {self.data_envio}"
    
    
class Chat(models.Model):
    car = models.ForeignKey(Car, related_name='chats', on_delete=models.CASCADE)
    comprador = models.ForeignKey(User, related_name='comprador_chats', on_delete=models.CASCADE)
    vendedor = models.ForeignKey(User, related_name='vendedor_chats', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Chat entre {self.comprador.username} e {self.vendedor.username} sobre {self.car.model}'
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensagem de {self.sender.username} em {self.created_at}'