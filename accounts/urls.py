from django.conf.urls import url
from . import views # from current folder import views


app_name = 'accounts'
urlpatterns = [
    
    url(r'^$', views.index, name="index"),
    # First argument https://django-amra0760.c9users.io/accounts/($ adds nothing)
    # Second argument display views.index
    # Third argument gave url a name
    
    url(r'^(?P<website_id>[0-9]+)/$', views.detail, name='detail'),
    # https://django-amra0760.c9users.io/passwordsecure/0 or 1 or 2 or 3....9 (question id number)
    
    
    url(r'website/add/$', views.WebsiteCreate.as_view(), name='website-add'),
    # /passwordsecure/website/add/
    
    url(r'website/(?P<pk>[0-9]+)/$', views.WebsiteUpdate.as_view(), name='website-update'),
    # /passwordsecure/website/#/
    
    url(r'website/(?P<pk>[0-9]+)/delete/$', views.WebsiteDelete.as_view(), name='website-delete'),
    # /passwordsecure/website/add/
    ]