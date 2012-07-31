# Title:  Django project for the ML4HMT 2011 workshop website
# Author: Christian Federmann <cfedermann@dfki.de>

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # Basic home page describing the ML4HMT workshops and shared tasks.
  url(r'^$',
    'ml4hmt.views.home', name='home'),

  url(r'^(?P<page_id>call-for-papers)/$',
    'ml4hmt.views.page', name='call-for-papers'),


## cfedermann: temporarily disabled until ML4HMT-12 data is prepared.
##
##  url(r'^(?P<page_id>program)/$',
##    'ml4hmt.views.page', name='program'),

  # Information about META Work Package 2.
  url(r'^(?P<page_id>meta-wp2)/$',
    'ml4hmt.views.page', name='meta-wp2'),

  # cfedermann: removed registration as workshop is over :)
  #  url(r'^signup/$',
  #    'ml4hmt.views.signup', name='signup'),
  #  url(r'^thank-you/$',
  #    'ml4hmt.views.thank_you', name="thank-you"),
  #  url(r'^participants/$',
  #    'ml4hmt.views.participants', name='participants'),
  #url(r'^admin/',
  #  include(admin.site.urls)),

  # Archived pages for the ML4HMT-11 workshop.
  url(r'^(?P<page_id>2011/call-for-papers)/$',
    'ml4hmt.views.page', name='call-for-papers-2011'),
  url(r'^(?P<page_id>2011/program)/$',
    'ml4hmt.views.page', name='program-2011'),

  # Prevent robots from indexing the website.
  url(r'^robots.txt$',
    'ml4hmt.views.robots', name='robots'),
)
