from django import forms
from .models import EngineerPost
from django_summernote.widgets import SummernoteWidget

class EngineerPostForm(forms.ModelForm):
    class Meta:
        model = EngineerPost
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