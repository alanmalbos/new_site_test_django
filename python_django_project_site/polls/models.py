from django.db import models

# Create your models here.

# model class to the questions
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('datetime publish')

    def __str__(self):
        return self.question_text

# model class to the choices
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    number_of_votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text