from rest_framework import serializers
from .models import BookModel

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['id','mualif','name','info','price','image','created_at','updated_at']
        read_only_fields = ['id','created_at','updated_at']