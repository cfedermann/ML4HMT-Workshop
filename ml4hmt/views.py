# Title:  Django project for the ML4HMT 2011 workshop website
# Author: Christian Federmann <cfedermann@dfki.de>

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ml4hmt.workshop.forms import ParticipantForm
from ml4hmt.workshop.models import Participant
from ml4hmt.settings import URL_PREFIX

def home(request):
    context = {'URL_PREFIX': URL_PREFIX}
    return render_to_response('home.html', context)

def page(request, page_id):
    """Renders a page for the workshop."""
    context = {'URL_PREFIX': URL_PREFIX}
    return render_to_response('{0}.html'.format(page_id), context)

def signup(request):
    """Creates a signup form for interested participants."""
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            new_participant = Participant(name=cleaned_data['name'],
              email=cleaned_data['email'],
              affiliation=cleaned_data['affiliation'])
            new_participant.save()
            uuid = new_participant.uuid
            return HttpResponseRedirect(reverse('thank-you'))
    
    else:
        form = ParticipantForm()
    
    context = {'form': form, 'URL_PREFIX': URL_PREFIX}
    return render_to_response('participants/signup.html', context,
       context_instance=RequestContext(request))

def thank_you(request):
    context = {'message': 'Thanks for participating in the ML4HMT ' \
      'workshop. See you soon!', 'URL_PREFIX': URL_PREFIX}
    return render_to_response('home.html', context) 
