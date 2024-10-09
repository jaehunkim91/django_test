from django.db import models


class User(models.Model):
    """
    회원 정보 테이블
    """
    user_id = models.AutoField(primary_key=True, help_text="회원 고유 키")

    name = models.CharField(max_length=100, help_text="이름")

    class Meta:
        db_table = "user"


