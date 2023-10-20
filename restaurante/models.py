from django.db import models
from datetime import datetime

class Cardapio(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False, default='')
    descricao = models.TextField(null=False, blank=False, default='')
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    pedacos = models.IntegerField(verbose_name="Pedaços", default=8)
    preco = models.DecimalField(verbose_name="Preço", max_digits=5, decimal_places=2, default=0.0)
    data_adicao = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.nome


