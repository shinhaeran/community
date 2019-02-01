from django.contrib import admin
from django.urls import path, include
from . import views

app_name='business'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('edit/<int:post_id>', views.edit, name='edit'),
    path('delete/<int:post_id>', views.delete, name='delete'),
]