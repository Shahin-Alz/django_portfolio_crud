from django import forms 
from .models import Portfolio
from .models import Filter

class portfolioForm(forms.ModelForm):

    class Meta:
        model= Portfolio
        fields = '__all__'

class filterForm(forms.ModelForm):

    class Meta:
        model= Filter
        fields = '__all__'