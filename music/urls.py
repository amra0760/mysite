from django.conf.urls import url, include
from . import views


app_name = 'music'

    
    
urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # /music/#(album id)
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    # /music/abum/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name="album-add"),
    
    ]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # urlpatterns = [
#     # /music/
#     url(r'^$', views.index, name='index'),
    
#     # /music/#(album id)
#     url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    
#     # /music/#/favorite
#     # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
#     ]