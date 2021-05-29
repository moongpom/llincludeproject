from django.contrib import admin
from .models import Post
# 1) .models에서 Post임포트
admin.site.register(Post)
# 2) admin 사이트에 Post 모델 테이블을 등록한다