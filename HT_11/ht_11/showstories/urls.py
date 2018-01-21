from django.urls import path, re_path
from showstories import views


urlpatterns = [
    re_path('^$', views.index, name='index'),
    path('<int:story_id>/', views.story_detail, name = 'story_detail'),
]