from django.shortcuts import render

#import a loader to load the templates
from django.template import loader, RequestContext

#import a HttpResponse to return the index page
from django.http import HttpResponse

#import models to work with the database
from .models import Question

# Create your views here.

# define a index page
def index(request):

    # get the last five questions created
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    # get the new template for index page
    template = loader.get_template('polls/index.html')

    # pass the data to template with a dictionary
    context = {
            'latest_questions': latest_questions,
        }

    # pass the template with the data to render in screen
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse('This is a question detail view of the question: %s' % question_id)

def results(request, question_id):
    return HttpResponse('These are a question results view of the question: %s' % question_id)

def vote(request, question_id):
    return HttpResponse('Vote on question: %s' % question_id)