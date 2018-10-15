from django.shortcuts import render
#import a HttpResponse to return the index page
from django.http import HttpResponse
# Create your views here.

# define a index page
def index(request):
    return HttpResponse('This is the index page of this application!')

def detail(request, question_id):
    return HttpResponse('This is a question detail view of the question: %s' % question_id)

def results(request, question_id):
    return HttpResponse('These are a question results view of the question: %s' % question_id)

def vote(request, question_id):
    return HttpResponse('Vote on question: %s' % question_id)