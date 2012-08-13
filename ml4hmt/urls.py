# Title:  Django project for the ML4HMT 2011 workshop website
# Author: Christian Federmann <cfedermann@dfki.de>

from django.conf.urls.defaults import patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # Basic home page describing the ML4HMT workshops and shared tasks.
  url(r'^$',
    'ml4hmt.views.home', name='home'),

  url(r'^(?P<page_id>call-for-papers)/$',
    'ml4hmt.views.page', name='call-for-papers'),

  url(r'^(?P<page_id>shared-task/es-en/apertium)/$',
    'ml4hmt.views.markup_page', name='shared-task-es-en-apertium'),
  url(r'^(?P<page_id>shared-task/es-en/lucy)/$',
    'ml4hmt.views.markup_page', name='shared-task-es-en-lucy'),
  url(r'^(?P<page_id>shared-task/es-en/moses)/$',
    'ml4hmt.views.markup_page', name='shared-task-es-en-moses'),

  # Information about META Work Package 2.
  url(r'^(?P<page_id>meta-wp2)/$',
    'ml4hmt.views.page', name='meta-wp2'),

  # Archived pages for the ML4HMT-11 workshop.
  url(r'^(?P<page_id>2011/call-for-papers)/$',
    'ml4hmt.views.page', name='call-for-papers-2011'),
  url(r'^(?P<page_id>2011/program)/$',
    'ml4hmt.views.page', name='program-2011'),

  # Prevent robots from indexing the website.
  url(r'^robots.txt$',
    'ml4hmt.views.robots', name='robots'),
)
