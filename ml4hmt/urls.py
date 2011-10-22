# Title:  Django project for the ML4HMT 2011 workshop website
# Author: Christian Federmann <cfedermann@dfki.de>

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'ml4hmt.views.home', name='home'),
  url(r'^(?P<page_id>call-for-papers)/$', 'ml4hmt.views.page', name='page'),
  url(r'^signup/$', 'ml4hmt.views.signup', name='signup'),
  url(r'^thank-you/$', 'ml4hmt.views.thank_you', name="thank-you"),
    # Examples:
    # url(r'^$', 'ml4hmt.views.home', name='home'),
    # url(r'^ml4hmt/', include('ml4hmt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)