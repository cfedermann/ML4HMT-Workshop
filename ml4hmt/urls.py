# Title:  Django project for the ML4HMT 2011 workshop website
# Author: Christian Federmann <cfedermann@dfki.de>

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

URL_PREFIX = 'ml4hmt/'

urlpatterns = patterns('',
  url(r'^{0}$'.format(URL_PREFIX),
    'ml4hmt.views.home', name='home'),
  url(r'^{0}(?P<page_id>call-for-papers)/$'.format(URL_PREFIX),
    'ml4hmt.views.page', name='call-for-papers'),
  url(r'^{0}(?P<page_id>program)/$'.format(URL_PREFIX),
    'ml4hmt.views.page', name='program'),
  url(r'^{0}signup/$'.format(URL_PREFIX),
    'ml4hmt.views.signup', name='signup'),
  url(r'^{0}thank-you/$'.format(URL_PREFIX),
    'ml4hmt.views.thank_you', name="thank-you"),
  url(r'^{0}admin/'.format(URL_PREFIX),
    include(admin.site.urls)),
)
