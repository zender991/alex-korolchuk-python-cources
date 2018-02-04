from django.urls import path, re_path
from news import views


app_name = 'news'
urlpatterns = [
    re_path('^$', views.get_stories, name='get_stories'),
    path('<int:story_id>/', views.story_detail, name='story_detail'),
    path('get_data/', views.get_data, name='get_data'),

]