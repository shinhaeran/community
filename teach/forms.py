from django import forms
from .models import TeachPost

class TeachPostForm(forms.ModelForm):
    class Meta:
        model = TeachPost
        fields = ('title', 'content',)