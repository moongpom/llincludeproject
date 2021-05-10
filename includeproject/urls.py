from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('staticapp/', include('staticapp.urls')),
    path('mediaformapp/', include('mediaformapp.urls')),
    path('admin/', admin.site.urls),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #static 사용
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media 사용
