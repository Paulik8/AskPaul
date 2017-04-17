from django.conf.urls import url

from ask.views import AboutView

urlpatterns = [
    url(r'^about$', AboutView.as_view(), name='about'),
]
