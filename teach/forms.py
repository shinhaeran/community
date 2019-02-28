from django import forms
from .models import TeachPost, TeachComment
from django_summernote.widgets import SummernoteWidget

class TeachPostForm(forms.ModelForm):
    class Meta:
        model = TeachPost
        fields = ( 'title', 'content',)
    
    title = forms.CharField(required=True, max_length=300,
        widget=forms.TextInput(attrs={
            'class': 'new-title',
            'placeholder': 'Title',
        })
    )
    content = forms.CharField(
        widget=SummernoteWidget(attrs={
            'placeholder': 'Content',
        })
    )

class TeachAdminPostForm(forms.ModelForm):
    class Meta:
        model = TeachPost
        fields = ('notice', 'title', 'content',)
    title = forms.CharField(required=True, max_length=300,
        widget=forms.TextInput(attrs={
            'class': 'new-title',
            'placeholder': 'Title',
        })
    )
    content = forms.CharField(
        widget=SummernoteWidget(attrs={
            'placeholder': 'Content',
        })
    )

class TeachCommentForm(forms.ModelForm):
    class Meta:
        model = TeachComment
        fields = ('text',)