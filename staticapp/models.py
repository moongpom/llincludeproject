from django.db import models

class Blog(models.Model):
  title = models.CharField(max_length = 200, default = '제목 없음')
  # 1)models의 CharFiled 타입으로 title생성. 최대 길이는 200이고 default값음 '제목없음'
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True) 
  def __str__(self):
    return self.title
  class Meta:
    ordering = ['-created_at']