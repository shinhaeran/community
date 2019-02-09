from django import forms
from .models import ElectronicPost
from django_summernote.widgets import SummernoteWidget

class ElectronicPostForm(forms.ModelForm):
    class Meta:
        model = ElectronicPost
        fields = ('title', 'content',)
        title = forms.CharField(required=True, max_length=300,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title',
        })
    )
    content = forms.CharField(
        widget=SummernoteWidget(attrs={
            'placeholder': 'Content',
        })
    )