from django.shortcuts import render
from .models import AndroidApp
from .serializers import AndroidAppSerializer
from rest_framework import generics

# Create your views here.

class AddAppView(generics.CreateAPIView):
    queryset = AndroidApp.objects.all()
    serializer_class = AndroidAppSerializer

class GetAppView(generics.ListAPIView):
    queryset =AndroidApp.objects.all()
    serializer_class=AndroidAppSerializer
    lookup_field ="id"

class DeleteAppView(generics.DestroyAPIView):
    queryset =AndroidApp.objects.all()
    serializer_class =AndroidAppSerializer
    lookup_field ="id"
