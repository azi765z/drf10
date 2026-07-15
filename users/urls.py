from django.urls import path
from . import views

urlpatterns = [
    path('userspro/', views.UserProList.as_view()),
    path('userpro/create/', views.UserProCreate.as_view()),
    path('userpro/update/<int:pk>/', views.UserProUpdate.as_view()),
    path('userpro/delete/<int:pk>/', views.UserProDelete.as_view()),
    path('userpro/<int:pk>/', views.UserProViews.as_view()),
]
