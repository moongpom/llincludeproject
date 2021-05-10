from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from datetime import datetime
from django.utils import timezone

# Create your views here.
def index(request):
  blog_list = Blog.objects.all()
  return render(request,'index.html', {'blogs':blog_list})

def new (request):
  if request.method == 'POST': #수정
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.created_at = timezone.datetime.now()
    blog.save()
    return redirect('/staticapp/')
  else:                        #새로 작성
    return render(request, 'static_new.html')

def detail(request, blog_id):
  blog = get_object_or_404(Blog, pk = blog_id)
  return render(request,'static_detail.html', {'blog':blog})

def edit(request, blog_id):
  blog = get_object_or_404(Blog, pk = blog_id)
  if request.method == 'POST':
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.created_at = timezone.datetime.now()
    blog.save()
    return redirect('/staticapp/blog/'+str(blog_id))
  else:
    return render(request, 'static_edit.html', {'editblog':blog})

def delete(request, blog_id):
  blog = Blog.objects.get(pk = blog_id)
  blog.delete() 
  return redirect('/staticapp/')