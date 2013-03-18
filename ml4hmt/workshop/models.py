# Title:  Django project for the ML4HMT 2012 workshop website
# Author: Christian Federmann <cfedermann@gmail.com>

from django.db import models
from uuid import uuid1

def _generate_UUID():
    """Generates a UUID1 as unique identifier for a participant instance."""
    new_id = uuid1().hex
    while Participant.objects.filter(uuid=new_id).exists():
        new_id = uuid1().hex
    return new_id

class Participant(models.Model):
    """Used to collect information about interested participants."""
    name = models.CharField(max_length=50, help_text="Your name")
    email = models.EmailField(help_text="An email address we can use " \
      "to contact you")
    affiliation = models.CharField(max_length=50, blank=True,
      help_text="Your affiliation (optional)")
    
    # These fields will be filled automatically!
    uuid = models.CharField(max_length=32, default=_generate_UUID)
