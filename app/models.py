"""
Definition of models.
"""

from django.db import models


class Person(models.Model):
    id = models.IntegerField (primary_key=True) # Уникальный Идентификатор пользователя в БД
    FirstName = models.CharField(max_length=30, blank = false, null = True) # Имя
    FamilyName = models.CharField(max_length=30, blank = false, null = True) # Фамилия
    PatronomycName = models.CharField(max_lenght = 30, blank = true, null = True) # Отчество
    BirthDate =models.DateField (blank = false, default=date.today) # Дата рождения