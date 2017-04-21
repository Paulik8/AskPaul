from django.shortcuts import render
from django.utils import timezone
#from ask_khotin.models import Question
from ask.forms import NameForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from django.views.generic.base import TemplateView

class AboutView(TemplateView):
	template_name = "about.html"
class MainView(TemplateView):
	template_name="base_auth.html"

class SettingsView(TemplateView):
	template_name="settings.html"

class HotView(TemplateView):
	template_name="listing.html"

class TagView(TemplateView):
	template_name="listingpotegu.html"

class OneQueView(TemplateView):
	template_name="onequestion.html"

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
	    data = ""
            for x in form.cleaned_data:
                data = data + str(form.cleaned_data[x]) + "<br />"
            return HttpResponse("Hello, %s" % data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/about/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
#def question_list(request):
#	questions = Question(text="What?", published_date=timezone.now())
#	questions = Question.objects.order_by('published_date')
##	questions = []
##	for i in xrange(1,30):
##		questions.append({
##			'title': 'title' + str(i),
##			'id': i,
##			'text': 'text' + str(i),
##		})
#	return render(request, 'base_auth.html', {'questions': questions})	

class LoginView(TemplateView):
	template_name="login.html"

class SignupView(TemplateView):
	template_name="signup.html"

class AskView(TemplateView):
	template_name="ask.html"
