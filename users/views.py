from django.shortcuts import render
from rest_framework import viewsets
from .models import UserModel
from .serializer import UserProtSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.


class UserProList(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserProtSerializer
    
class UserProCreate(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserProtSerializer

class UserProUpdate(RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserProtSerializer
    
class UserProDelete(RetrieveDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserProtSerializer
    
class UserProViews(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserProtSerializer