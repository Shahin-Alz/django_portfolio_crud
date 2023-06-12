from django import forms 
from .models import About

class AboutForm(forms.ModelForm):

    degree = (
        ('junior', 'Junior'),
        ('master', 'Master'),
        ('senior', 'Senior'),
    )
    degree = forms.ChoiceField(choices=degree)


    class Meta:
        model= About
        fields = '__all__'

