from django.shortcuts import render

#import a HttpResponse to return the index page
from django.http import HttpResponse

#import models to work with the database
from .models import Question

# Create your views here.

# define a index page
def index(request):

    # get the last five questions created
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    # create a string with de questions text
    output = ', '.join(q.question_text for q in latest_questions)
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse('This is a question detail view of the question: %s' % question_id)

def results(request, question_id):
    return HttpResponse('These are a question results view of the question: %s' % question_id)

def vote(request, question_id):
    return HttpResponse('Vote on question: %s' % question_id)