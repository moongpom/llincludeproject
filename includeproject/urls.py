from django.contrib import admin
from django.urls import path, include #include를 사용하기위해 import하기
from django.conf import settings
from django.conf.urls.static import static

"""
프로젝트 단위로 url을 관리하면 가독성이 떨어지고 유지보수가 힘들다.
따라서 장고 url이 제공하는 include함수를 사용하여 앱 별로 url 관리하는 게 좋다. 
"""
urlpatterns = [
    path('staticapp/', include('staticapp.urls')),
    path('mediaformapp/', include('mediaformapp.urls')),
    path('admin/', admin.site.urls),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #static 사용
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media 사용
