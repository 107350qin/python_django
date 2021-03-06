from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
	question_text=models.CharField('问题',max_length=200)
	pub_date=models.DateTimeField('时间')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField('内容',max_length=200)
	votes=models.IntegerField('投票',default=0)

	def __str__(self):
		return self.choice_text