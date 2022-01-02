"""
Definition of models.
"""

from django.db import models


class Person(models.Model):
    id = models.IntegerField (primary_key=True) # Уникальный Идентификатор пользователя в БД
    FirstName = models.CharField(max_length=30) # Имя
    FamilyName = models.CharField(max_length=30) # Фамилия
    PatronomycName = models.CharField(max_lenght = 30, ) # Отчество
    BirthDate =models.DateField () # Дата рождения