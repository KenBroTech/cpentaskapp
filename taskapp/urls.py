from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='taskapp-index'), 
    path('about/', views.about, name='taskapp-about'),
    path('delete/<int:pk>/', views.delete, name='taskapp-delete'),
    path('update/<int:pk>/', views.update, name='taskapp-update'),
]

