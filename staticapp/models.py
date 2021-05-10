from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length = 200, default = '제목 없음')
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True) #생성시간 자동저장

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-created_at']