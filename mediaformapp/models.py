from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length = 200)
  content = models.TextField()
  image = models.ImageField()
  created_at = models.DateTimeField(auto_now_add = True) #생성시간 자동저장

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-created_at'] #최신글이 맨 위에 오도록 정렬