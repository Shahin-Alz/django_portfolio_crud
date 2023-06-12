from django import forms 
from .models import Skills

class skillsForm(forms.ModelForm):

    class Meta:
        model= Skills
        fields = '__all__'