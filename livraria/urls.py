from django.urls import path
from livraria.views import inicio

urlpatterns = [
    path('', inicio)
]
