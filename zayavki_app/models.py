from django.db import models

# Create your models here.
from django.db import models

class Zapros(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В обработке'),
        ('done', 'Выполнена'),
    ]

    topic = models.CharField(max_length=200, verbose_name="Тема")
    description = models.TextField(verbose_name="Описание")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.topic
    
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
