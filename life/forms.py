from django import forms
from .models import LifePost

class LifePostForm(forms.ModelForm):
    class Meta:
        model = LifePost
        fields = ('title', 'content',)