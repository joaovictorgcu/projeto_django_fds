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



class Mensagem(models.Model):
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    carro = models.ForeignKey(Car, null=True, blank=True, on_delete=models.SET_NULL)
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Mensagem de {self.remetente} para {self.destinatario} sobre {self.carro}'

