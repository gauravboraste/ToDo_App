
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete_task/<str:pk>/', views.deleteTask,name="delete"),
     path('update_Task/<str:pk>/', views.update_Task,name="update_Task"),
]