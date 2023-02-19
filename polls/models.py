import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
# db 에는 Question, Choice 두 엔티티가 있다
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    # 지금부터 하루전
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#     q=Question.objects.get(pk=1)  // primary key set to 1
#     q.was_published_recently()    // boolean

# q=Question.objects.get(question_text='hey')
# q

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
