from django.db import models
from django.contrib.auth import get_user_model

# Django에서 현재 사용 중인 사용자 모델을 가져옵니다.
User = get_user_model()

# Post 모델을 정의합니다.
class Post(models.Model):
    # 게시물의 제목을 저장하는 필드입니다. 최대 길이는 20자입니다.
    title = models.CharField(max_length=20)
    # 게시물의 내용을 저장하는 필드입니다. 텍스트 필드를 사용합니다.
    content = models.TextField()
    # 게시물을 작성한 사용자를 저장하는 외래 키 필드입니다.
    # User 모델과의 관계를 나타내며, 사용자가 삭제되면 관련된 게시물도 삭제됩니다.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    # 객체를 문자열로 나타낼 때 사용할 표현을 정의합니다. 여기서는 게시물의 제목을 반환합니다.
    def __str__(self):
        return self.title
