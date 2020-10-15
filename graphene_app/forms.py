from .models import *
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = '__all__'
