from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question 
# from django.template import loader, RequestContext


# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5] # sorts by date
    # # output = ", ".join(q.question_text for q in latest_questions) # iterate over every question and split by comma
    
    # template = loader.get_template('polls/index.html') # links to template
    # context = RequestContext(request,{
    #     'latest_questions': latest_questions
    # })
    
    # shortcut
    context = {
        'latest_questions': latest_questions,
    }
    return render(request, 'polls/index.html', context)
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # returns 404 error if the question doesn't exist
    return render(request, 'polls/detail.html', {'question': question})
    
    # question_dict = {
    #     'question',question,
    # }
    # return render(request, 'polls/detail.html', question_dict)
    
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html',{'question': question, 'error_message': "Please select a choice.",})
        # return render(request, 'polls/detail.html',{'question': question, 'error_message': "Please select a choice.",})
    else:
        # increase votes by 1
        selected_choice.votes += 1
        selected_choice.save()
        # returns user to results page
        # return HttpResponseRedirect(reverse'polls:results', args=(question.id,)))
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
    
    
    
    
    