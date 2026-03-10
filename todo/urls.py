from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name = 'addTask'),
    path('markDone/<int:pk>/', views.markDone, name='markDone'),
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
    path('markUndone/<int:pk>/', views.markUndone, name='markUndone'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task')
]