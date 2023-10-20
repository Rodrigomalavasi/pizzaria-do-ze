from django.shortcuts import render
from restaurante.models import Cardapio

def index(request):
    itens = Cardapio.objects.all()

    return render(request, 'restaurante/index.html', {'itens': itens})
