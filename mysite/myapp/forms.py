from django import forms

from .models import Logger
from .models import Timer

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'

class TimerForm(forms.ModelForm):
    class Meta:
        model = Timer
        fields = '__all__'