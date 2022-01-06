import datetime

from django.db import models

class Person(models.Model):
    FirstName = models.CharField (max_length=50, verbose_name = 'Имя') ## Имя
    SecondName = models.CharField (max_length=50, verbose_name = 'Фамилия') ## Фамилия
    PatronymicName = models.CharField (max_length=50, blank=True, verbose_name = 'Отчетсво') ## Отчество
    BirthDate = models.DateField (verbose_name = 'Дата рождения') ## Дата рождения 
    
    def __str__(self):
        return self.FirstName
        return self.SecondName
        return self.PatronymicName
        return self.BirthDate
