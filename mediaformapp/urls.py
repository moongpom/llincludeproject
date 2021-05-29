from django.urls import path
# 1) django.urls에서 path를 import해온다
# 1-1) path():  urlpatterns에 포함 할 요소를 반환한다.
from . import views
# 2) 현재 폴더의 views를 임포트한다

app_name = "mediaformapp"
# 3) 앱의 이름을 "mediaformapp"으로 설정(namespace)

urlpatterns = [
# 4) Client로 부터 요청이 들어오면 그 요청을 보낼 경로를 정의한 리스트
  path('', views.home, name="home"),
  # 5) 주소는 공란이고(주소의 첫페이지) views.home 파일을 실행한다. 이때 name을 home로 지정하여 전체파일명 대신 쓸 수 있다.
  path('post/new', views.new, name="new"),
  # 6) 주소는 post/new이고 views.new 파일을 실행한다. 이때 name을 new로 지정하여 전체파일명 대신 쓸 수 있다.
  path('post/<int:post_id>', views.detail, name="detail"),
  # 7) 주소는 post/<int:post_id>이고 views.detail 파일을 실행한다. 이때 name을 detail로 지정하여 전체파일명 대신 쓸 수 있다.
  path('post/edit/<int:post_id>', views.edit, name="edit"),
  # 8) 주소는 post/edit/<int:post_id>이고 views.edit 파일을 실행한다. 이때 name을 edit으로 지정하여 전체파일명 대신 쓸 수 있다.
  path('post/delete/<int:post_id>', views.delete, name="delete"),
  # 9) 주소는 post/delete/<int:post_id>이고 views.delete 파일을 실행한다. 이때 name을 delete로 지정하여 전체파일명 대신 쓸 수 있다.
]