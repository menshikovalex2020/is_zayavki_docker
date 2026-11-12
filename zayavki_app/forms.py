from django import forms
from .models import Zapros

class ZaprosForm(forms.ModelForm):
    class Meta:
        model = Zapros
        fields = ['topic', 'description', 'status']
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
