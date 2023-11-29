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

