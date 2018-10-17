from django.shortcuts import render, get_object_or_404

#import a loader to load the templates
from django.template import loader

#import models to work with the database
from .models import Question

# Create your views here.

# define a index page
def index(request):

    # get the last five questions created
    latest_questions = Question.objects.order_by('-pub_date')[:5]

    # pass the data to template with a dictionary
    context = {
            'latest_questions': latest_questions,
        }

    # pass the template with the data to render in screen
    return render(request, 'polls/index.html',context)

# define a detail question page
def detail(request, question_id):
    # get a question passed by request
    question = get_object_or_404(Question, pk = question_id)

    # pass the question data to template with a dictionary
    context = {'question':question}

    # call the template
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    return HttpResponse('These are a question results view of the question: %s' % question_id)

def vote(request, question_id):
    return HttpResponse('Vote on question: %s' % question_id)