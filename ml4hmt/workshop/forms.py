# Title:  Django project for the ML4HMT 2012 workshop website
# Author: Christian Federmann <cfedermann@gmail.com>

from django.forms import ModelForm
from ml4hmt.workshop.models import Participant

# pylint: disable-msg=R0924
class ParticipantForm(ModelForm):
    """Form to collect information about interested participants."""
    class Meta:
        model = Participant
        exclude = ('uuid',)