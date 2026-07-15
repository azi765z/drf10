from django.shortcuts import render
from rest_framework import viewsets
from .models import BookModel
from .serializer import BookSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.

class BookList(ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    
class BookCreate(CreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

class BokkUpdate(RetrieveUpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

class BookDelete(RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    
class BookUpdateDestroyAPIView(RetrieveDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    

    