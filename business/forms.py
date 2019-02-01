from django import forms
from .models import BusinessPost

class BusinessPostForm(forms.ModelForm):
    class Meta:
        model = BusinessPost
        fields = ('title', 'content',)