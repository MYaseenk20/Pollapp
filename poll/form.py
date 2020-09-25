from django.forms import ModelForm
from .models import *

class poll_form(ModelForm):
    class Meta:
        model=Poll
        fields=['poll_one','poll_two','poll_third','message']
