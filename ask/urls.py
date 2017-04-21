from django.conf.urls import url

#from ask.views import AboutView
from . import views

urlpatterns = [
    	url(r'^about/$', views.AboutView.as_view(), name='about'),
	url(r'^$', views.MainView.as_view(), name="base"),
	#url(r'^$', views.question_list, name="base"),
	url(r'^hot/$', views.HotView.as_view(), name="hot"),
	url(r'^tag/(?P<tag>[a-z]+)/$', views.TagView.as_view(), name="tag"),
	url(r'^question/(?P<urlquestion>[0-9]+)/$', views.OneQueView.as_view(), name="onequestion"),
	url(r'^login/$', views.LoginView.as_view(), name="login"),
	url(r'^signup/$', views.SignupView.as_view(), name="signup"),
	url(r'^ask/$', views.AskView.as_view(), name="ask"),
	url(r'^settings/$', views.SettingsView.as_view(), name="settings"),
	url(r'^your_name/$', views.get_name),
]
