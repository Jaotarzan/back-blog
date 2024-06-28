from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from blog.models import Animal
from blog.serializers import AnimalSerializer

# Create your views here.
class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer