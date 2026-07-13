from django.shortcuts import render
from rest_framework import viewsets
from .models import UserModel
from .serializer import UserProtSerializer

# Create your views here.


class UserProView(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserProtSerializer