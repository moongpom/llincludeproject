from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from datetime import datetime
from django.utils import timezone

# Create your views here.
def home(request):
  post_list = Post.objects.all()
  return render(request,'home.html', {'posts':post_list})

def new(request):
  if request.method == 'POST': #글을 작성한 후 저장 버튼을 눌렀을 때
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
      post = post_form.save(commit = False)
      post.created_at = timezone.now() #날짜 생성
      post.save()
      return redirect('home')
  else:                       #글을 쓰려고 들어갔을 때
    post_form = PostForm()
    return render(request, 'post_new.html', {'post_form':post_form})

def detail(request, post_id):
  post = get_object_or_404(Post, pk = post_id)
  return render(request,'post_detail.html', {'post':post})

def edit(request, post_id):
  post = get_object_or_404(Post, pk = post_id)
  if request.method == 'GET': #수정하려고 들어갔을 때
    post_form = PostForm(instance = post)
    return render(request, 'post_edit.html', {'edit_post':post_form})
  else:                       #글을 수정하고 수정버튼을 눌렀을 때
    post_form = PostForm(request.POST, request.FILES, instance = post)
    if post_form.is_valid():
      post = post_form.save(commit=False)
      post.created_at = timezone.now()
      post.save()
    return  redirect('/mediaformapp/post/'+str(post_id))

def delete(request, post_id):
  post = Post.objects.get(pk = post_id)
  post.delete() 
  return redirect('/mediaformapp/')