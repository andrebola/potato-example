from django.conf.urls import *
from django.conf import settings
from core import views

urlpatterns = patterns('',
    url(r'^$', views.posts, name='posts'),
    url(r'^post/add/', views.create_post, name='new_post'),
    url(r'^post/edit/(?P<key>[-\w]+)/$', views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<key>[-\w]+)/$', views.delete_post, name='delete_post'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
        url(r'^404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
    )
