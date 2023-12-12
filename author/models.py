from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    born_to = models.DateField()
    nickname = models.CharField(max_length=60, blank=True)

    def __str__(self) -> str:
        return f'{self.name} -> {self.nickname}'