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
  """
  * http 메소드 중 GET과 POST

  GET은 url에 parameter들을 포함하여 보내고, 길이에 제한이 있습니다.
  POST는 url에 parameter들이 보이지 않게 보냅니다.
  POST로는 보이면 안 되거나 길이가 긴 정보들을 보내면 좋습니다.
  그래서 글의 내용들을 넘겨줄 때(저장하겠다고 요청을 보낼 때) POST를 사용합니다.
  """

  if request.method == 'POST': #글을 작성한 후 저장 버튼을 눌렀을 때
    post_form = PostForm(request.POST, request.FILES) 
    if post_form.is_valid():
      post = post_form.save(commit = False)
      post.created_at = timezone.now() #날짜 생성
      post.save()
      return redirect('home')
  else:                       #글을 쓰려고 들어갔을 때
    post_form = PostForm() #글을 입력받기 위한 빈 form을 불러옴
    return render(request, 'post_new.html', {'post_form':post_form})

def detail(request, post_id):
  post = get_object_or_404(Post, pk = post_id)
  return render(request,'post_detail.html', {'post':post})

def edit(request, post_id):
  post = get_object_or_404(Post, pk = post_id)
  if request.method == 'GET': #수정하려고 들어갔을 때
    post_form = PostForm(instance = post) #현재 post가 포함된 form을 불러옴
    return render(request, 'post_edit.html', {'edit_post':post_form})
  else:                       #글을 수정하고 수정버튼을 눌렀을 때
    post_form = PostForm(request.POST, request.FILES, instance = post) #현재 post에 가져온 정보를 form에 담음
    if post_form.is_valid():
      post = post_form.save(commit=False)
      post.created_at = timezone.now()
      post.save()
    return  redirect('/mediaformapp/post/'+str(post_id))

def delete(request, post_id):
  post = Post.objects.get(pk = post_id)
  post.delete() 
  return redirect('/mediaformapp/')