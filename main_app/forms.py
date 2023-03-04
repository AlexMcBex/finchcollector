from django.forms import ModelForm
from .models import Ribbon

class RibbonForm(ModelForm):
    class Meta:
        model= Ribbon
        fields = ['date', 'color']
