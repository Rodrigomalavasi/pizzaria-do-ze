from django.contrib import admin
from restaurante.models import Cardapio

class ListandoCardapio(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'preco','data_adicao')
    list_display_links = ('nome',)
    search_fields = ("nome",)

admin.site.register(Cardapio, ListandoCardapio)
