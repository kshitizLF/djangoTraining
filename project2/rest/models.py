from django.db import models

# Create your models here.
class Car(models.Model):
    company = models.CharField(max_length=40)
    model = models.CharField(max_length=40)