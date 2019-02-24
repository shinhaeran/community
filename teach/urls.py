from django.contrib import admin
from django.urls import path, include
from . import views

app_name='teach'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('edit/<int:post_id>', views.edit, name='edit'),
    path('delete/<int:post_id>', views.delete, name='delete'),
    path('delete/<int:post_id>/deleteComment/<int:comment_id>', views.remove_comment, name='delete_comment'),
    path('<int:post_id>/addComment', views.add_comment_to_post, name='addComment'),
    path('<int:comment_id>/addReComment', views.add_comment_to_comment, name='addReComment'),
]