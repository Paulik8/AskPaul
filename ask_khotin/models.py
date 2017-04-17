#from datetime import datetime
#from django.db import models
#from django.contrib.auth.models import User

#GOOD_RATING = 10

#class Profile(models.Model):
#	avatar = models.ImageField(uploads_to="avatars/")
#	user = models.OneToOneField(User)

#class QuestionManager(models.Manager):
#	def best_questions(self):
#		return self.filter(rating__gt=GOOD_RATING).order_by(['-rating'])
#	def new_questions(self):
#		return self.order_by('-created_at')

#class Question(models.Model):
#	title = models.CharField(max_length=60)
#	text = models.TextField()
#	author = models.ForeignKey(User)
#	rating = models.IntegerField()
#	created_at = models.DateTimeField(default=datetime.now)
#	tags = models.ManyToManyFiels('Tag')	
#	objects = QuestionManager()
#		
#	def nice_title(self):
#		return self.title + '?'
#	def __unicode__(self):	
#		return u'{0} - {1}'.format(self.id, self.title)

#class Tag(models.Model):
#	name = models.CharFiels(max_length=60)
