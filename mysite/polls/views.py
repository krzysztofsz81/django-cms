from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Contact

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[0:5]

    return render(request, "polls/index.html", {
        'latest_questions': latest_questions,
    })

def contacts(request):
    all_contacts = Contact.objects.order_by('-forename')[0:5]
    return render(request, "polls/contacts.html", {
        'contacts': all_contacts,
    })

def contact(request, contact_id):
    contact_detail = get_object_or_404(Contact, pk = contact_id)
    return render(request, "polls/contact.html", {
        'contact': contact_detail,
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {
        'question': question,
    })

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
        'question': question,
    })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Please select a choice',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))