from django.db import models


class Author(models.Model):
    """
    작가
    """
    author_id = models.AutoField(primary_key=True, help_text="작가 고유 키")
    name = models.CharField(max_length=100, help_text="작가 명")

    class Meta:
        db_table = "author"


class Book(models.Model):
    """
    책
    """
    book_id = models.AutoField(primary_key=True, help_text="회원 고유 키")
    name = models.CharField(max_length=100, help_text="책 이름")
    author_id = models.ForeignKey(
        to=Author, on_delete=models.DO_NOTHING,  help_text="작가", null=False
    )

    class Meta:
        db_table = "book"
