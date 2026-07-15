from django.urls import path
from .views import BookUpdateDestroyAPIView,BookList,BookCreate,BokkUpdate,BookDelete


urlpatterns = [
    path('cars/', BookList.as_view()),
    path('cars/create/', BookCreate.as_view()),
    path('cars/<int:pk>/update/', BokkUpdate.as_view()),
    path('cars/<int:pk>/delete/', BookDelete.as_view()),
    path('cars/<int:pk>/detail/', BookUpdateDestroyAPIView.as_view()),
]