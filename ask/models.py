from datetime import datetime
from django.utils import timezone
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from ask.paginator import PaginatorClass
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.http import Http404
from django.db.models import Count

GOOD_RATING = 10
class Question(models.Model):
    user = models.ForeignKey('Profile')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    tag = models.ManyToManyField('Tag')

    def __str__(self):
        return "{} {} {} {}".format(self.id, self.title, self.rating, self.pub_date)


class Answer(models.Model):
    user = models.ForeignKey('Profile')
    question = models.ForeignKey('Question')
    text = models.TextField()
    rating = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)

    def notify(self):
        data = {'id': self.id, 'user': self.user.id, 'text': self.text, 'rating': self.rating, 'correct': self.correct, }

    def __str__(self):
        return "{} {}".format(self.question.title, self.pub_date)


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class Profile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=255, default=0)
    #avatar = models.ImageField(upload_to='uploads', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.nickname)


class Like(models.Model):
    content_type = models.ForeignKey(ContentType, related_name="content_type_likes")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey('Profile')
    like = models.BooleanField()

    def __str__(self):
        return "{} {} {} {} {}".format(self.content_type, self.user, self.object_id, self.content_object, self.like)
