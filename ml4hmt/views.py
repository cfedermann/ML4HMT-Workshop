# Title:  Django project for the ML4HMT 2011 workshop website
# Author: Christian Federmann <cfedermann@dfki.de>

from os.path import basename
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from ml4hmt.workshop.forms import ParticipantForm
from ml4hmt.workshop.models import Participant
from ml4hmt.settings import URL_PREFIX

def robots(request):
    """Disallows robot access to some pages."""
    _robots = ['User-agent: *']
    
    # The following URLs should NOT be crawled by bots, so we disallow access!
    for url in ('signup', 'thank-you', 'participants', 'admin'):
        _robots.append('Disallow: {0}/{1}/'.format(URL_PREFIX, url))
    
    return HttpResponse('\n'.join(_robots), mimetype='text/plain')

def home(request):
    """Renders the home page for the workshop."""
    context = {'URL_PREFIX': URL_PREFIX}
    return render_to_response('home.html', context)

def page(request, page_id):
    """Renders a page for the workshop."""
    context = {'URL_PREFIX': URL_PREFIX}
    return render_to_response('{0}.html'.format(page_id), context)

def markup_page(request, page_id):
    """Renders a page containing Markdown markup for the workshop."""
    markup = render_to_string('{0}.markdown'.format(page_id), {})
    title = basename(page_id).capitalize()
    context = {'URL_PREFIX': URL_PREFIX, 'markup': markup, 'title': title}
    return render_to_response('markdown.html', context)

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
            _uuid = new_participant.uuid
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

def participants(request):
    """Renders a list of participants for the workshop."""
    _participants = Participant.objects.all()
    context = {'participants': _participants, 'URL_PREFIX': URL_PREFIX}
    return render_to_response('participants/participants.html', context)