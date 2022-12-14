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
"""
class Users(models.Model):
    #id - django само
    #local_id = models.DecimalField(max_digits=5, decimal_places=0) # локальный id для подтвержденных users(пользователей)
    username = models.CharField(max_length=255, default='ЧеловекОшибка') # имя пользователя
    role = models.CharField(max_length=255, default='client') # роль (client, worker, admin(он же инженер))
    activity = models.BooleanField(default=True) # статус подтвержденности пользователя


class Client(models.Model):
    #id - django само
    username = models.CharField(max_length=255, default='ЧеловекОшибка') # имя пользователя
    cards = models.CharField(max_length=255, default=None) # банковские карты (debit, credit)
    balance_debit = models.DecimalField(max_digits=10, decimal_places=2, default=0) # максимум на балансе 99 999 999, 99
    balance_credit = models.DecimalField(max_digits=7, decimal_places=2, default=0) # максимум на балансе кредитки 99 999, 99
    #money_transfer_create = models.DateTimeField(auto_now_add=True)
    #money_transfer_update = models.DateTimeField(auto_now=True)

     #def __str__(self):
     #   return self.title
"""