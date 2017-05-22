from datetime import datetime
from django.utils import timezone
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from ask.paginator import PaginatorClass

GOOD_RATING = 10

class Profile(models.Model):
	avatar = models.ImageField()#uploads_to="avatars/"
	user = models.OneToOneField(User)

class QuestionManager(models.Manager):
	def best_questions(self):
		return self.filter(rating__gt=GOOD_RATING).order_by(['-rating'])
	def new_questions(self):
		return self.order_by('-created_at')
class Question2Manger(models.Manager):
	def getQuestionsBy(self,request):
		questions = Question2.objects.all()
		page = request.GET.get('page')
		return render(request, 'base.html', {'questions': questions,'paginator':PaginatorClass.paginate(questions,page)})

class Question(models.Model):
	title = models.CharField(max_length=60)
	text = models.TextField(default=0)
	author = models.ForeignKey(User, default=0)
	rating = models.IntegerField(default=0)
	created_at = models.DateTimeField(default=datetime.now)
	tags = models.ManyToManyField('Tag')	
	objects = QuestionManager()
		
	def nice_title(self):
		return self.title + '?'
	def __unicode__(self):	
		return u'{0} - {1}'.format(self.id, self.title)

class Tag(models.Model):
	name = models.CharField(max_length=60)

class Question2(models.Model):
	text = models.TextField(max_length=200, null=True)
	published_date = models.DateTimeField('date published', null=True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.text
	
