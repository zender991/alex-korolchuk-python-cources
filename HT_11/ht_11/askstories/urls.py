#from django.conf.urls import patterns, url

from django.urls import path, re_path

from askstories import views

# urlpatterns = patterns('',
#     url(r'^$', views.index, name='index')
# )

urlpatterns = [
    #path('index/', views.index, name='index'),
    re_path('^$', views.index, name='index'),
]