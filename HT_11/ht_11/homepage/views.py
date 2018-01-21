from django.shortcuts import render
from homepage.request_data import execute


def index(request):

    return render(request, 'homepage/homepage.html')


def get_data(request):
    execute()

    return render(request,'homepage/homepage.html')
