from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """Пользователи."""

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    USER_CHOICES = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    )

    email = models.EmailField('Почта', unique=True)
    bio = models.TextField('Инфо', blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField('Наименование', max_length=256)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Наименование', max_length=256)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Наименование', max_length=256)
    year = models.IntegerField('Год')
    description = models.CharField('Описание', max_length=200, blank=True)
    genre = models.ManyToManyField(Genre,
                                   verbose_name='Жанр')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField('Отзыв')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField('Рейтинг')
    pub_date = models.DateTimeField('Дата', auto_now_add=True)
    title_id = models.ForeignKey(Title,
                                 verbose_name='Произведение',
                                 on_delete=models.CASCADE,
                                 related_name='reviews')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField('Комментарий')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Дата', auto_now_add=True)
    review_id = models.ForeignKey(Review,
                                  verbose_name='Отзыв',
                                  on_delete=models.CASCADE,
                                  related_name='comments')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text
