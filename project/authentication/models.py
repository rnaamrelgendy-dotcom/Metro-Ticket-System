from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.TextChoices):
    manager = 'manager'
    passenger = 'passenger'

class User(AbstractUser):
    role = models.CharField(max_length=50 , choices=Role.choices , default= Role.passenger)

    def __str__(self):
        return self.username