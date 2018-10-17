from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

# import a loader to load the templates
from django.template import loader

# import a reverse
from django.urls import reverse

# import models to work with the database
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
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', { 'question' : question })

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        select_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/index.html', { 'question' : question, 'error_message' : 'Please select a choice'})
    else:
        select_choice.number_of_votes += 1
        select_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args = (question.id, )))