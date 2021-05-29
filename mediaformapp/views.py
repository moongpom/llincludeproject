from django.shortcuts import render
# 1)django.shortcuts에서 render함수를 임포트 해온다 
# 1-1) render라는 함수란?
#render는 템플릿을 불러온다(페이지만 띄울 수 있음)
#request를 받고 response를 보내줄 때 페이지에 데이터를 같이 보내는 역할로 render를 쓴다
#주어진 템플릿에 주어진 정보를 결합한 뒤 응답을 보낸다.

from django.shortcuts import redirect 
# 2)django.shortcuts에서 redirect함수를 임포트 해온다 
# 2-1) redirect라는 함수란?
# redirect는 url로 이동한다(다른페이지로 이동하지만 데이터는 보내지 않음) 
#redirect 실행 후  url에 맞는 views가 함수가 다시 실행된다(  render을 할 지 redirect를 할지 함수에 따라 다시 결정함)

from django.shortcuts import get_object_or_404 
# 3)django.shortcuts에서get_object_or_404 를 임포트 해온다
# 3-1) get_object_404라는 함수란?
#404라는게 객체를 가져오든가 / 없는거면 찾을 수 없다는 예외를 처리해 줄 수 있다는 뜻을 의미한다

from .models import Post
# 4).models에서 Post를 임포트 해온다
from .forms import PostForm
# 5) .forms에서 PostForm을 임포트해온다
from datetime import datetime
# 6) datetime에서 datetime을 임포트해온다
from django.utils import timezone
# 7) django.utils에서 timezone을 임포트해온다


def home(request):
# 8) 데이터처리를 위한 home이라는 함수. 요청받고 응답을 보낸다. 이 앱에서는 첫번째 홈페이지를 뜻한다
# 8-1)request란? 이 함수의 응답을 생성하는데 사용되는 요청 개체이다.
  post_list = Post.objects.all()
  # 9)Post 객체의 모든것을 post_list에 담는다
  return render(request,'home.html', {'posts':post_list})
  # 10)home.html에 posts딕셔너리 정보를 결합한 뒤 응답을 보낸다

def new(request):
# 11) 데이터처리를 위한 new라는 함수. 요청받고 응답을 보낸다. 이 앱에서는 게시물을 생성할 때 사용한다
  """
  * http 메소드 중 GET과 POST

  GET은 url에 parameter들을 포함하여 보내고, 길이에 제한이 있습니다.
  POST는 url에 parameter들이 보이지 않게 보냅니다.
  POST로는 보이면 안 되거나 길이가 긴 정보들을 보내면 좋습니다.
  그래서 글의 내용들을 넘겨줄 때(저장하겠다고 요청을 보낼 때) POST를 사용합니다.
  """

  if request.method == 'POST': 
  # 12) 응답받은 method가 POST라면
    post_form = PostForm(request.POST, request.FILES) 
    # 13) 응답받은 POST와 FILES를 받은 PostForm을 post_form으로 생성해준다
    #(요청받은 정보들을 새로운 객체의 컬럼에 저장하기 위해 새로운 객체 생성)

    if post_form.is_valid():
    # 14) post_form이 유효하다면
      post = post_form.save(commit = False)
      # 15) 임시저장을 해준다(commit속성으로 나타낼 수 있고 보통 form에 없는 필드가 있을 때 임시저장한다)
      post.created_at = timezone.now()
      # 16)폼에 없는 created_at 필드를 timezone.now()으로 생성해준다
      post.save()
      # 17)post 객체를 저장해준다

      
      return redirect('home') 
      
      # 18)home이라는 name으로 redirect해준다
      #여기서는 새로운 html을 만들어서 보내는게 아니라 기능을 작동후 원래 페이지로 돌아가야하기때문에 redirect

      #이거로 하면 namespace문제로 실행 안 됨->아래 셋 중 하나로 해주기

      #1. /mediaformapp/주소로 바로 보내기
      #return redirect('/mediaformapp/')
      #2.namespace인 mediaformapp를 붙여서 name이용하기
      #return redirect('mediaformapp:home')
      #3.새롭게 생성한 게시글의 detail로 이동한다
      # #return render(request,'post_detail.html', {'post':post})
      
  else:                       
  # 19) 12번에 이어서 응답받은 method가 POST가 아니라면 (GET이라면)
    post_form = PostForm() 
    # 20)요청받은 정보들을 새로운 객체의 컬럼에 저장하기 위해 새로운 객체 생성
    return render(request, 'post_new.html', {'post_form':post_form})
    # 21) post_form과  post_new.html을 결합하여 응답을 보낸다

def detail(request, post_id):
# 22)데이터처리를 위한 detail이라는 함수. 이 앱에서는 게시물의 세부글을 볼 때 사용한다.
# # 매개변수로 post_id가있어야한다
  post = get_object_or_404(Post, pk = post_id)
  # 23) 첫번째 매개변수로 우리가 가져와야할 테이블,두번째 매개변수는 pk (Primary Key 즉, 데이터베이스에서의 id)를 
  #가져오는데 못가져올 경우 예외를 처리해준다
  return render(request,'post_detail.html', {'post':post})
  # 24)post_detail.html에 post를 결합하여 응답을 보낸다

def edit(request, post_id):
# 25)  데이터처리를 위한 edit이라는 함수. 이 앱에서는 게시물을 수정할 때 사용한다.
# # 매개변수로 post_id가있어야한다
  post = get_object_or_404(Post, pk = post_id)
  # 26) 첫번째 매개변수로 우리가 가져와야할 테이블,두번째 매개변수는 pk (Primary Key 즉, 데이터베이스에서의 id)를 
  #가져오는데 못가져올 경우 예외를 처리해준다
  if request.method == 'GET': 
  # 27)만약 요청받은 mothod가 GET이라면
    post_form = PostForm(instance = post) 
    # 28)요청받은 정보들을 새로운 객체의 컬럼에 저장하기 위해 새로운 객체를 생성한다(이때 객체는 post)
    return render(request, 'post_edit.html', {'edit_post':post_form})
    # 29)post_edit.html에 edit_post를 결합하여 요청에 대한 응답을 보낸다
  else:                       
  # 30)요청받은 mothod가 POST이라면
    post_form = PostForm(request.POST, request.FILES, instance = post) 
    # 31)요청받은 정보들을 새로운 객체의 컬럼에 저장하기 위해 새로운 객체를 생성한다
    #이때 요청받은 메소드와 파일,post를 다 받아온다
    if post_form.is_valid():
      post = post_form.save(commit=False)
      post.created_at = timezone.now()
      post.save()
    return  redirect('/mediaformapp/post/' + str(post_id))
    # 32)/mediaformapp/post/+ str(post_id) 주소로 redirect해준다. 수정한 게시글로 돌아간다
    #33)옆이 공백인데 이 부분에 str은 왜 필요한가? 
    # 33)변환기를 명시해주어 다른 문자와 구별하기 위해서

def delete(request, post_id):
# 34)데이터처리를 위한 delete이라는 함수. 이 앱에서는 게시물을 삭제할 때 사용한다.
# # 매개변수로 post_id가있어야한다
  post = Post.objects.get(pk = post_id)
  # 35)pk(기본키)값이 post_id인 객체를 post라는 이름에 저장한다
  post.delete() 
  # 36)내장함수  delete를 사용하여 post를 삭제한다
  #return redirect('/mediaformapp/')
  return redirect('mediaformapp:home')
  # 37)mediaformapp:home로 redirect해준다. 홈페이지로 돌아간다