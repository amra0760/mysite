from django.shortcuts import render

from django.http import HttpResponse

from d

from .models import Question 

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5] # sorts by date
    # output = ", ".join(q.question_text for q in latest_questions) # iterate over every question and split by comma
    
    
    
    return HttpResponse(output)
    
def detail(request, question_id):
    return HttpResponse("This is the detail view of the question: %s" % question_id)
    
def results(request, question_id):
    return HttpResponse("These are the results of the question: %s" % question_id)
    
def vote(request, question_id):
    return HttpResponse("Vote on question: %s" % question_id)