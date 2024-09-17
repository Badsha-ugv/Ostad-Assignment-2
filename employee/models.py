from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, unique=True)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    designation = models.CharField(max_length=100)
    short_desc = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}- {self.designation}'
