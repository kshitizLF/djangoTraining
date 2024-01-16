from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    age = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email},{self.age}"

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default = timezone.now)

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=3)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f"Option {self.choice_text} has {self.votes} votes"
