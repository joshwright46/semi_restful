from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows/new$', views.shows_new),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<id>\d+)$', views.id),
    url(r'^shows$', views.shows),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit),
    url(r'^shows/(?P<id>\d+)/destroy', views.destroy),
    url(r'^shows/(?P<id>\d+)/update', views.update)
    
]