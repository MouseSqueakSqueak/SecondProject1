import datetime

from django.db import models

class Person(models.Model):
    FirstName = models.CharField (max_length=50)
    SecondName = models.CharField (max_length=50)
    PatronymicName = models.CharField (max_length=50, blank=True)
    BirthDate = models.DateField ()
    
    def __str__(self):
        return self.FirstName
        return self.SecondName
        return self.PatronymicName
        return self.BirthDate
