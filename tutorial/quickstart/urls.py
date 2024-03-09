from django.urls import path
from .views import DigimonList

urlpatterns = [
    path('digimon/', DigimonList.as_view(), name='digimon-list'),
]