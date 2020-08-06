from django.db import models


# Create your models here.

class Data(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateTimeField()
    email=models.EmailField()
    investigation=models.CharField(max_length=100)
    history=models.CharField(max_length=100)

