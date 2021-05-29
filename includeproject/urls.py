from django.contrib import admin
# 1) django.contrib에서 admin을 import해온다
from django.urls import path, include 
# 2) django.urls에서 path, include를 import해온다
# 2-1) path(): urlpatterns에 포함 할 요소를 반환한다.
# 2-2) include(): 다른앱안의  urls파일의 path들을 포함할 수 있게 해준다
from django.conf import settings
# 3) django.conf 에서 settings를 임포트한다
from django.conf.urls.static import static
# 4) django.conf.urls.static에서 static을 임포트한다
# 4-1) static(): 디버그 모드에서 파일을 제공하기위한 URL 패턴을 반환하는 도우미 함수이다
import staticapp.views
# 5) staticapp에 있는views 파일 임포트

"""
프로젝트 단위로 url을 관리하면 가독성이 떨어지고 유지보수가 힘들다.
따라서 장고 url이 제공하는 include함수를 사용하여 앱 별로 url 관리하는 게 좋다. 
"""
urlpatterns = [ 
# 6)Client로 부터 요청이 들어오면 그 요청을 보낼 경로를 정의한 리스트
    path('', staticapp.views.index, name="index"),
    # 7) 주소는 공란이고(주소의 첫페이지) staticapp.views.index 파일을 실행한다. 이때 name을 index로 지정하여 전체파일명 대신 쓸 수 있다.
    path('staticapp/', include('staticapp.urls')),
    # 8) 'staticapp.urls'를 포함하며 staticapp/ 주소뒤에 staticapp.urls가 붙는다
    path('mediaformapp/', include('mediaformapp.urls')),
    # 9) 'mediaformapp.urls'를 포함하며 mediaformapp/ 주소뒤에 mediaformapp.urls가 붙는다
    path('admin/', admin.site.urls),
    # 10) 주소창에 admin을 치면 admin을 연결한다. 
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
# 11) urlpatterns에 static파일에 대한 URL패턴을 반환한다
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# 12) urlpatterns에 media파일에 대한 URL패턴을 반환한다
