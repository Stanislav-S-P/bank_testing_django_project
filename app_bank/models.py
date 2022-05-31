from django.contrib.auth.models import User
from django.db import models


class BankTestModel(models.Model):
    """
    Класс - модель таблицы создания вопросов для тестирования
    """
    question = models.CharField(max_length=500, verbose_name='Вопрос')
    first_answer = models.CharField(max_length=500, verbose_name='Первый вариант')
    second_answer = models.CharField(max_length=500, verbose_name='Второй вариант')
    third_answer = models.CharField(max_length=500, verbose_name='Третий вариант')
    correct_answer = models.CharField(max_length=500, verbose_name='Правильный ответ')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class UserAnswer(models.Model):
    """
       Класс - модель таблицы ответов пользоватлеей на тестировании
    """
    STATUS_CHOICES = [
        ('корректный', 'корректный'),
        ('не корректный', 'не корректный'),
    ]
    user = models.ForeignKey(
        User, null=True, blank=True, related_name='user_answer', on_delete=models.CASCADE, verbose_name='Пользователь'
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')
    question = models.CharField(max_length=500, verbose_name='Вопрос')
    answer = models.CharField(max_length=500, verbose_name='Ответ')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='не корректный', verbose_name='Корректность ответа'
    )

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'
