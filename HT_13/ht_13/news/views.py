from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Story, Category
from news.request_data import execute


def get_stories(request):
    askstories_list = Story.objects.filter(category_id=1).order_by('title')[:5]

    newstories_list = Story.objects.filter(category_id=2).order_by('title')[:5]


    jobstories_list = Story.objects.filter(category_id=3).order_by('title')[:5]


    showstories_list = Story.objects.filter(category_id=4).order_by('title')[:5]

    return render(request, 'news/results.html', {'askstories_list': askstories_list, 'newstories_list': newstories_list,
                                                 'jobstories_list': jobstories_list, 'showstories_list': showstories_list})





def story_detail(request, story_id):
    story = get_object_or_404(Story, pk=story_id)

    return render(request, 'news/details.html', {'story': story})



def index(request):

    return render(request, 'news/index.html')


def get_data(request):
    execute()

    return render(request, 'news/results.html')
    #redirect('news/results.html')
    #render_to_response('news/results.html')