from django.urls import path
from restaurante.views import index

urlpatterns = [
    path('', index)
]
