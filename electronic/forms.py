from django import forms
from .models import ElectronicPost

class ElectronicPostForm(forms.ModelForm):
    class Meta:
        model = ElectronicPost
        fields = ('title', 'content',)