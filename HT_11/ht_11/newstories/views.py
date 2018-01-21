from django.shortcuts import render, get_object_or_404
from newstories.models import Newstories


def index(request):
    titles_list = Newstories.objects.all().order_by('title')[:5]

    context = { 'titles_list': titles_list }
    return render(request, 'newstories/index.html', context)


def story_detail(request, story_id):
    newstory = get_object_or_404(Newstories, pk=story_id)

    return render(request, 'newstories/story_detail.html', {'newstory': newstory})

