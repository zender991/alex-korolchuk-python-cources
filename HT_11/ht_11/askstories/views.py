from django.shortcuts import render, get_object_or_404
from askstories.models import Askstories
from django.http import HttpResponse
from django.http import Http404

def index(request):
    titles_list = Askstories.objects.all().order_by('title')[:5]

    context = { 'titles_list': titles_list }
    return render(request, 'askstories/index.html', context)


def story_detail(request, story_id):
    askstory = get_object_or_404(Askstories, pk=story_id)

    return render(request, 'askstories/story_detail.html', {'askstory': askstory})

