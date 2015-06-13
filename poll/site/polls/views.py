from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.views import generic
from .models import Poll, Choice

# Create your views here.

def index(request):
    latest_question_list = Poll.objects.all().order_by('-pub_date')
    # version 1
    # output = ','.join([p.question for p in latest_question_list])
    # return HttpResponse(output)

    # version 2
    # template = loader.get_template('polls/index.html')
    # context = Context({'latest_question_list':latest_question_list,
    #                    })
    # return HttpResponse(template.render(context))

    # version 3
    # return render_to_response('polls/index.html',
    #                           {
    #                             'latest_question_list':latest_question_list,
    #                           })

    return render(request, 'polls/index.html',
                  {
                      'latest_question_list':latest_question_list,
                  })

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Poll.objects.all().order_by('-pub_date')

def detail(request, poll_id):
    # version 1
    # try:
    #     poll = Poll.objects.get(pk=poll_id)
    #
    # except Poll.DoesNotExist:
    #     raise Http404
    # return render_to_response('polls/detail.html', {'poll': poll})

    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {
                          'poll': poll,
                          'error_message': "You didn't select a choice."
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))
