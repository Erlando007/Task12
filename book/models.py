from django.db import models
from author.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=60)
    created_at = models.DateField()
    genre = models.CharField(max_length=80)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self) -> str:
        return f'{self.title} -> {self.author}'