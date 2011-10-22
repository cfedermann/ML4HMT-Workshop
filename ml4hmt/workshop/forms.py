# Title:  Django project for the ML4HMT 2011 workshop website
# Author: Christian Federmann <cfedermann@dfki.de>

from django.forms import ModelForm
from ml4hmt.workshop.models import Participant

class ParticipantForm(ModelForm):
    """Form to collect information about interested participants."""
    class Meta:
        model = Participant
        exclude = ('uuid',)