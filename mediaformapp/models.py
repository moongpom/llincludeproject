from django.db import models
# 1) django.db에서 models임포트해옴
class Post(models.Model):
  title = models.CharField(max_length = 200)
  # 2)models의 CharFiled로 title 필드 추가 이때 길이 제한 200줌
  content = models.TextField()
  # 3) models의 TextFiled로 content 필드 추가
  image = models.ImageField()
  # 4)models의 ImageFiled로 image 필드 추가 
  created_at = models.DateTimeField(auto_now_add = True)
  # 5)models.DateTimeField 사용하여 created_at 필드 추가 이때  auto_now_add 속성은 생성일자에 대한 속성으로
  #   auto_now_add=True 는 django model 이 최초 저장 시에만 현재날짜(date.today()) 를 적용한다
  #cf.수정일자 : auto_now=True(django model 이 save 될 때마다 현재날짜(date.today()) 로 갱신

# title, content, image, created_at는 필드
# 필드는 데이터베이스 테이블에 저장하길 원하는 데이터 열(컬럼)
  def __str__(self):
    # 6) 객체를 문자열로 표현한 것을 반환해주는 함수이다
    return self.title
    # 7)객체를 title로 반환해둔다
  class Meta:
    # Meta 내부 클래스를 정의해 모델에 대한 메타데이터를 정의
    # 테이블의 필드는 모델 클래스의 속성으로 정의하고 필드 이외에 항목은 Meta 내부 클래스의 속성으로 정의
    # Meta 내부 클래스 속성 중 하나인 ordering(정렬)
    ordering = ['-created_at'] 
    # 8)순서를 생성순서 반대로 정렬