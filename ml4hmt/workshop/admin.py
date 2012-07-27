# Title:  Django project for the ML4HMT 2012 workshop website
# Author: Christian Federmann <cfedermann@dfki.de>

from django.contrib import admin
from ml4hmt.workshop.models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    """Administration interface for participants."""
    list_display = ('name', 'email', 'affiliation')
    search_fields = ('name', 'affiliation')

admin.site.register(Participant, ParticipantAdmin)