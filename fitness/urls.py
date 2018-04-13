from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_exercises, name='all_exercises'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_exercise, name='delete_exercise')
]
