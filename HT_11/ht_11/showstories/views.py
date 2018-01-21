from django.shortcuts import render, get_object_or_404
from showstories.models import Showstories


def index(request):
    titles_list = Showstories.objects.all().order_by('title')[:5]

    context = { 'titles_list': titles_list }
    return render(request, 'showstories/index.html', context)


def story_detail(request, story_id):
    showstory = get_object_or_404(Showstories, pk=story_id)

    return render(request, 'showstories/story_detail.html', {'showstory': showstory})

