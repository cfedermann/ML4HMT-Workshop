# Title:  Django project for the ML4HMT 2012 workshop website
# Author: Christian Federmann <cfedermann@gmail.com>

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
    # for url in ('admin',):
    #    _robots.append('Disallow: {0}/{1}/'.format(URL_PREFIX, url))
    
    return HttpResponse('\n'.join(_robots), mimetype='text/plain')

def home(request):
    """Renders the home page for the workshop."""
    context = {'URL_PREFIX': URL_PREFIX}
    return render_to_response('home.html', context)

def _page_not_found(request, template_name='404.html'):
    """Custom HTTP 404 handler that preserves URL_PREFIX."""
    context = {'URL_PREFIX': URL_PREFIX, 'request_path': request.path}
    return render_to_response('404.html', context)

def _server_error(request, template_name='500.html'):
    """Custom HTTP 500 handler that preserves URL_PREFIX."""
    context = {'URL_PREFIX': URL_PREFIX, 'request_path': request.path}
    return render_to_response('500.html', context)

def page(request, page_id):
    """Renders a page for the workshop."""
    context = {'URL_PREFIX': URL_PREFIX}
    if page_id == 'call-for-papers':
        from datetime import date
        context.update({'gogogo': date.today() > date(2012, 8, 22)})
    return render_to_response('{0}.html'.format(page_id), context)

def markup_page(request, page_id):
    """Renders a page containing Markdown markup for the workshop."""
    markup = render_to_string('{0}.markdown'.format(page_id), {})
    title = basename(page_id).capitalize()
    context = {'URL_PREFIX': URL_PREFIX, 'markup': markup, 'title': title}
    return render_to_response('markdown.html', context)
