from django.urls import path, re_path
from homepage import views


urlpatterns = [
    re_path('^$', views.index, name='index'),
]