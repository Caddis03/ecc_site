from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class AboutView(generic.ListView):
    model = Question
    template_name = "polls/about.html"
    
class GivingView(generic.ListView):
    model = Question
    template_name = "polls/giving.html"
    
class MinistriesView(generic.ListView):
    model = Question
    template_name = "polls/ministries.html"
    
class ContactView(generic.ListView):
    model = Question
    template_name = "polls/contact.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",
                      {
                          "question": question,
                          "error_message": "You didn't select a choice."
                      },
                    )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

# Create your views here.
