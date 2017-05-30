
from __future__ import unicode_literals

from django.contrib import admin
from ask.models import Question, Answer, Tag, Profile

admin.site.register(Question)
admin.site.register(Answer) 
admin.site.register(Tag) 
admin.site.register(Profile) 

# Register your models here.
