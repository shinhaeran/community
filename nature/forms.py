from django import forms
from .models import NaturePost, NatureComment
from django_summernote.widgets import SummernoteWidget

class NaturePostForm(forms.ModelForm):
    class Meta:
        model = NaturePost
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

class NatureAdminPostForm(forms.ModelForm):
    class Meta:
        model = NaturePost
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

class NatureCommentForm(forms.ModelForm):
    class Meta:
        model = NatureComment
        fields = ('text',)