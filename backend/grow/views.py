from django.shortcuts import render
from rest_framework import viewsets
from .models import Grow
from .serializers import GrowSerializer

# Create your views here.

class GrowViewSet(viewsets.ModelViewSet):
    queryset = Grow.objects.all()
    serializer_class = GrowSerializer