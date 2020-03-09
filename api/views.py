from django.shortcuts import render
from .models import movie
from .serializers import movieSerializer
from rest_framework import viewsets

# Create your views here.

class movieView(viewsets.ModelViewSet):
	qs = movie.objects.all()
	serializer_class = movieSerializer
