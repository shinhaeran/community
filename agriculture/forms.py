from django import forms
from .models import AgriculturePost

class AgriculturePostForm(forms.ModelForm):
    class Meta:
        model = AgriculturePost
        fields = ('title', 'content',)