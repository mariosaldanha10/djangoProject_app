from django.http import HttpResponseRedirect
from .models import Choice, Question
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


# We’re using two generic views here: ListView and DetailView. Respectively, those two views abstract the concepts of
# “display a list of objects” and “display a detail page for a particular type of object.”
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

    # this class was created to future questions appear in the index and so users cannot reach them if they know
    # or guess the right URL.
    class DetailView(generic.DetailView):
        ...

        def get_queryset(self):
            """
            Excludes any questions that aren't published yet.
            """
            return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# dummy implementation of voted function created
from django.db import connection, transaction


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice_id = request.POST['choice']
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    # Use parameterized queries to prevent SQL injection attacks
    with transaction.atomic():
        cursor = connection.cursor()
        cursor.execute("UPDATE polls_choice SET votes = votes + 1 WHERE id = %s", [choice_id])

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# after someone votes in a question, the vote() view redirects to the results page for the question.
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
