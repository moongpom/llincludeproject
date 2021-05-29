from django import forms 
# 1) django에서 forms 임포트해옴
from .models import Post
# 2).models에서 Post임포트해옴

class PostForm(forms.ModelForm): 
# 3) 장고에서 제공해주는 forms를 상수로 받아옴

  class Meta: 
  # 메타데이터를 제공하는 내부 클래스. 따라서 모델폼을 사용할 때 사용해준다.
  # 메타데이터: 어떤 목적을 가지고 만들어진 데이터
    model = Post 
    # 4)model이 Post라 지정
    fields = ['title', 'image', 'content'] 
    # 5) forms의 필드 리스트(데이터모델을 베이스로 필요한 필드들만)를 생성