from django.db import models
from Contas.models import ContaPadrao
from Produtos.models import Produtos
class Carrinho(models.Model):
    ESTADO = (
        ('A', 'Aberto'),
        ('F', 'Fechado'),
        ('C', 'Cancelado')
    )
    usuario = models.ForeignKey(ContaPadrao, on_delete=models.OneToOneField) # Usuário deletado, carrinho também.
    item    = models.TextField()# como dadano eu associo?
    estado  = models.TextField(choices=ESTADO, default='A')