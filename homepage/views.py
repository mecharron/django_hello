from django.shortcuts import render

from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    context = {'title': os.environ['TITLE']}
    return render(request, 'homepage/index.html', context)