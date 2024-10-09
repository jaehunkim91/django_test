from rest_framework import serializers

from content.models.book import Book, Author
from users.models.user import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_id', 'name']


class BookSerializer(serializers.ModelSerializer):

    author_id = AuthorSerializer(many=False)

    class Meta:
        model = Book
        fields = ['book_id', 'name', 'author_id',]
