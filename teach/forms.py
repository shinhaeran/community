from django import forms
from .models import TeachPost
from django_summernote.widgets import SummernoteWidget

class TeachPostForm(forms.ModelForm):
    class Meta:
        model = TeachPost
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