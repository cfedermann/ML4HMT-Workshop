# Title:  Django project for the ML4HMT 2011 workshop website
# Author: Christian Federmann <cfedermann@dfki.de>

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$',
    'ml4hmt.views.home', name='home'),
  url(r'^(?P<page_id>call-for-papers)/$',
    'ml4hmt.views.page', name='call-for-papers'),
  url(r'^(?P<page_id>program)/$',
    'ml4hmt.views.page', name='program'),
  url(r'^signup/$',
    'ml4hmt.views.signup', name='signup'),
  url(r'^thank-you/$',
    'ml4hmt.views.thank_you', name="thank-you"),
  url(r'^admin/',
    include(admin.site.urls)),
)
