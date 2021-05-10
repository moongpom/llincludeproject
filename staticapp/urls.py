from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('blog/new', views.new, name="new"),
  path('blog/<int:blog_id>', views.detail, name="detail"),
  path('blog/edit/<int:blog_id>', views.edit, name="edit"),
  path('blog/delete/<int:blog_id>', views.delete, name="delete"),
]