from rest_framework import serializers
from .models import Digimon

class DigimonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digimon
        fields = ['id', 'name']