import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_values(self):
        t = timezone.now() - datetime.timedelta(days=2,minutes=59,hours=23,seconds=59)
        q1 = Question(pub_date = t)
        self.assertIs(q1.was_published_recently(),True)

    def test_was_published_recently_with_old_values(self):
        t = timezone.now() - datetime.timedelta(days=3,minutes=1)
        q1 = Question(pub_date = t)
        self.assertIs(q1.was_published_recently(),False)