from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('room/', views.roomname),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
