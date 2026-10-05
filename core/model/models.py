from django.db import models

from pyclbr import Class

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Email: {self.email}")
