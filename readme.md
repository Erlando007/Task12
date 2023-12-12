1) **Создание Django-проект:**
   
   В терминале введите следующие команды:

   ```bash
   django-admin startproject config  #(название проекта)
   ```

2) **Создание приложения `author` и `book`:**
   
   ```bash
   python3 manage.py startapp author
   python3 manage.py startapp book
   ```

3) **Определение модели автора (`author/models.py`):**

   ```python
   from django.db import models

   class Author(models.Model):
    name = models.CharField(max_length=50)
    born_to = models.DateField()
    nickname = models.CharField(max_length=60, blank=True)

    def __str__(self) -> str:
        return f'{self.name} -> {self.nickname}'


   ```

4) **Определение модели книги (`book/models.py`):**

   ```python
    from django.db import models
    from author.models import Author

    class Book(models.Model):
        title = models.CharField(max_length=60)
        created_at = models.DateField()
        genre = models.CharField(max_length=80)
        author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self) -> str:
        return f'{self.title} -> {self.author}'
   ```

5) **Настройка приложения в `settings.py`:**

   В файле `homework_django/settings.py` добавьте в раздел `INSTALLED_APPS` ваши приложения:

   ```python
   INSTALLED_APPS = [
       # ...
       'author',
       'book',
   ]
   ```

6) **Выполнение миграции:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7) **Создание CRUD в файлах заметок (`notes.md`):**

   - **Create (Создание):**
     - Создание автора: `Author.objects.create(name='Имя', born_to ='2000-10-10', nickname='Псевдоним')`
     - Создание книги: 
       ```python
       author = Author.objects.get(name='Имя')
       Book.objects.create(title='Название книги', created_at='2000-10-12', genre='Жанр', author=author)
       ```

   - **Read (Чтение):**
     - Получение всех авторов: `Author.objects.all()`
     - Получение всех книг: `Book.objects.all()`
     - Получение книги по названию: `Book.objects.get(title='Название книги')`

   - **Update (Обновление):**
     - Обновление автора: 
       ```python
       author = Author.objects.get(name='Имя')
       author.nick_name = 'Новый псевдоним'
       author.save()
       ```
     - Обновление книги:
       ```python
       book = Book.objects.get(title='Название книги')
       book.genre = 'Новый жанр'
       book.save()
       ```

   - **Delete (Удаление):**
     - Удаление автора: `Author.objects.get(name='Имя').delete()`
     - Удаление книги: `Book.objects.get(title='Название книги').delete()`

