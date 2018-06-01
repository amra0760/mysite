from django.conf.urls import url
from . import views # from current folder import views


app_name = 'polls'
urlpatterns = [
    
    url(r'^$', views.index, name="index"),
    # First argument https://django-amra0760.c9users.io/polls/($ adds nothing)
    # Second argument display views.index
    # Third argument gave url a name
    
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # https://django-amra0760.c9users.io/polls/0 or 1 or 2 or 3....9 (question id number)
    
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # https://django-amra0760.c9users.io/polls/#/results
    
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # https://django-amra0760.c9users.io/polls/#/vote
    

    ]