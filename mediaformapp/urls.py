from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('post/new', views.new, name="new"),
  path('post/<int:post_id>', views.detail, name="detail"),
  path('post/edit/<int:post_id>', views.edit, name="edit"),
  path('post/delete/<int:post_id>', views.delete, name="delete"),
]