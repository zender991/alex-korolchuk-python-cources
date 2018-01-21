from django.shortcuts import render, get_object_or_404
from jobstories.models import Jobstories


def index(request):
    titles_list = Jobstories.objects.all().order_by('title')[:5]

    context = { 'titles_list': titles_list }
    return render(request, 'jobstories/index.html', context)


def story_detail(request, story_id):
    jobstory = get_object_or_404(Jobstories, pk=story_id)

    return render(request, 'jobstories/story_detail.html', {'jobstory': jobstory})

