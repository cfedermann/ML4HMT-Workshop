# Title:  Django project for the ML4HMT 2011 workshop website
# Author: Christian Federmann <cfedermann@dfki.de>

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ml4hmt.workshop.forms import ParticipantForm
from ml4hmt.workshop.models import Participant

def home(request):
    return render_to_response('home.html')

def page(request, page_id):
    """Renders a page for the workshop."""
    return render_to_response('{0}.html'.format(page_id))

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
            return HttpResponseRedirect('http://www.dfki.de/ml4hmt/thank-you/?uuid={0}'.format(uuid))
    
    else:
        form = ParticipantForm()
    
    context = {'form': form}
    return render_to_response('participants/signup.html', context,
       context_instance=RequestContext(request))

def thank_you(request):
    uuid = request.GET.get('uuid')
    context = {'message': 'We have saved your request, please note down your personal ID: <strong>{0}</strong>. We will contact you soon!'.format(uuid)}
    return render_to_response('home.html', context) 
