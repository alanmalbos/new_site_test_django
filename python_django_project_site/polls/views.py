from django.shortcuts import render
#import a HttpResponse to return the index page
from django.http import HttpResponse
# Create your views here.

# define a index page
def index(request):
    return HttpResponse('This is the index page of this application!')