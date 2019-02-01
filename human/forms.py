from django import forms
from .models import HumanPost

class HumanPostForm(forms.ModelForm):
    class Meta:
        model = HumanPost
        fields = ('title', 'content',)