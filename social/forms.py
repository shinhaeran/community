from django import forms
from .models import SocialPost, SocialComment
from django_summernote.widgets import SummernoteWidget

class SocialPostForm(forms.ModelForm):
    class Meta:
        model = SocialPost
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

class SocialAdminPostForm(forms.ModelForm):
    class Meta:
        model = SocialPost
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

class SocialCommentForm(forms.ModelForm):
    class Meta:
        model = SocialComment
        fields = ('text',)