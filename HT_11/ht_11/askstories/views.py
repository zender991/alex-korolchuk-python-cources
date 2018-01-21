#from django.http import HttpResponse
#from django.template import Context, loader
from django.shortcuts import render
from askstories.models import Askstories

def index(request):
    titles_list = Askstories.objects.all().order_by('title')[:5]

    context = { 'titles_list': titles_list }
    print(context)
    return render(request, 'askstories/index.html', context)
