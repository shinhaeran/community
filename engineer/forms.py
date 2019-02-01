from django import forms
from .models import EngineerPost

class EngineerPostForm(forms.ModelForm):
    class Meta:
        model = EngineerPost
        fields = ('title', 'content',)