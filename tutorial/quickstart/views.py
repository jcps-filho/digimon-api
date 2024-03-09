from django.shortcuts import render
from rest_framework import generics
from .models import Digimon
from .serializers import DigimonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class DigimonList(generics.ListAPIView):
    queryset = Digimon.objects.all()
    serializer_class = DigimonSerializer

    def get(self, request, format=None):
        digimonName = request.query_params.get('name', 'Agumon')
        print(digimonName)
        # URL of the external API you want to fetch data from
        external_api_url = f'https://digimon-api.vercel.app/api/digimon/name/{digimonName}'
        response = requests.get(external_api_url)
        
        if response.status_code == 200:
            # Assuming the external API returns JSON data
            data = response.json()
            return Response(data)
        else:
            return Response({'error': 'Failed to fetch data from the external API'}, status=response.status_code)