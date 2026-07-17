from django.urls import path
from .views import BookUpdateDestroyAPIView,BookList,BookCreate,BokkUpdate,BookDelete


urlpatterns = [
    path('books/', BookList.as_view()),
    path('book/create/', BookCreate.as_view()),
    path('book/<int:pk>/update/', BokkUpdate.as_view()),
    path('book/<int:pk>/delete/', BookDelete.as_view()),
    path('book/<int:pk>/detail/', BookUpdateDestroyAPIView.as_view()),
    
]