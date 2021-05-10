from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'image', 'content'] #form을 띄워줄 때 title, image, content를 띄워줌