from django.urls import path
from .views import UserProView

urlpatterns = [
    path('users/', UserProView.as_view({'get': 'list', 'post': 'create'}), name='UserProView'),
]
