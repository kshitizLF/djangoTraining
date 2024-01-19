from django.db import models
from home.models import Employee

# Create your models here.
class Tasks(models.Model):
    text = models.TextField()
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
