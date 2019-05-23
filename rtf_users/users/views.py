from django.shortcuts import render
from .models import Usuario
from .serializer import UsuarioSerializer
from rest_framework import generics

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class= UsuarioSerializer

class UsuarioDelete(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class= UsuarioSerializer
    lookup_field= 'id'

class UsuarioUpdate(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class= UsuarioSerializer
    lookup_field= 'id'

class UsuarioGet(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class= UsuarioSerializer
    lookup_field='id'
