from django import forms
from .models import NaturePost

class NaturePostForm(forms.ModelForm):
    class Meta:
        model = NaturePost
        fields = ('title', 'content',)