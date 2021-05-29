### mediaformapp에 있는 view에 주석을 먼저 작성해보고 작성해주세요.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
# 1).models 에서 Blog 테이블을 임포트해온다
from datetime import datetime
from django.utils import timezone

def index(request):
# 2)index함수가 요청을받고 
  blog_list = Blog.objects.all()
  # 3)Blog.objects.all로 모든 객체를 blog_list에 담는다
  return render(request,'index.html', {'blogs':blog_list})
  # 4)blog_list를 blogs 딕셔너리에 저장하여 index.html와 결합한 뒤 응답을 보낸다

def new (request):
# 5)new함수가 요청을받고 
  if request.method == 'POST': 
  # 6)만약 요청받은 method가 POST라면
    blog = Blog()
    # 7)models에 정의된 클래스의 객체를 하나 생성한다
    blog.title = request.POST['title']
    # 8)생성한 blog객체의 title에 요청들어온(새로 작성한) title을 담는다
    blog.body = request.POST['body']
    # 9)생성한 blog객체의 body에 요청들어온(새로 작성한) body를 담는다
    blog.created_at = timezone.datetime.now()
    # 10)생성한 created_at에 timezone.datetime.now()로 작성일을 담는다
    blog.save()
    # 11)새로만든 객체를 저장해준다
   # return redirect('index')
    return redirect('/')
    # 12)첫 공백주소로 redirect해준다
  else:                       
  # 13)요청받은 method가 GET이라면(맨 처음 new가 실행될 때 페이지를 생성함)
    return render(request, 'static_new.html')
    # 14)'static_new.html'를 띄운다

def detail(request, blog_id):
# 15)detail이 요청을받고 id값을 받음
  blog = get_object_or_404(Blog, pk = blog_id)
  # 16)첫번째 매개변수로 우리가 가져와야할 테이블,두번째 매개변수는 pk (Primary Key 즉, 데이터베이스에서의 id)를 
  #가져오는데 못가져올 경우 예외를 처리해준다
  #가져온 객체를 blog에 담는다
  return render(request, 'static_detail.html', {'blog':blog})
  # 17)가져온 객체를 딕셔너리에 담아 'static_detail.html'와 결합시켜 응답을 보낸다

def edit(request, blog_id):
  # 18)edit가 요청 받고 id값을 받음
  blog = get_object_or_404(Blog, pk = blog_id)
  # 19)get_object_or_404로 해당하는 id에 맞는 객체를 blog에 담는다
  if request.method == 'POST':
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.created_at = timezone.datetime.now()
    blog.save()
    return redirect('/staticapp/blog/'+str(blog_id))
    # 20)/staticapp/blog/+str(blog_id)로 redirect보낸다.
    # 기능을 작동후 원래 페이지로 돌아가야하기때문에 redirect
  else:
    return render(request, 'static_edit.html', {'editblog':blog})
    # 21)가져온 객체를 editblog딕셔너리에 담아 'static_edit.html'와 결합시켜 응답을 보낸다

def delete(request, blog_id):
# 22)delete가 요청 받고 id값을 받음
  blog = Blog.objects.get(pk = blog_id)
  # 23)pk가 blog_id인 객체를 blog로 받아온다
  blog.delete() 
  # 24)받아온 blog를 삭제함
  return redirect('/')
  # 25)홈으로 redirect보낸다