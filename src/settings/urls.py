
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from angular.views import angular,delete,test,sweet,ajax,request,update,index
from angular import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test$', test),
    url(r'^ajax/$', ajax),
    url(r'^request/$', request),
    url(r'^sweet$', sweet),
    url(r'^$', index),
    url(r'^angular/$', angular,name='angular'),
    url(r'^delete/(\w+)/(\d+)/$', delete),
    url(r'^update/(\w+)/$', update),
    url(r'^api/$', views.ApiData.as_view()),
]
