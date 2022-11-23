from django.db import models

# Create your models here.
# models - базовый класс моделей на основе которых можно создавать свои модели таблиц баз данных
# https://ejudge.lksh.ru/lang_docs/djbook.ru/rel1.9/ref/models/fields.html
"""   пример:
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
"""
class Bank(models.Model):
    title = models.CharField(max_length=255)
    money_balance = models.DecimalField
    money_transfer_create = models.DateTimeField(auto_now_add=True)
    money_transfer_update = models.DateTimeField(auto_now=True)
#необходимо прописать константы ImageField MEDIA_ROOT, MEDIA_URL