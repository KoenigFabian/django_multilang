from . import views
from django.urls import path
from django.conf.urls import url

app_name = 'testapp'
urlpatterns = [
    path('', views.index, name='index'),
    #url(r'^$', views.index, name='index'),
]
