from django import forms
from .models import LifePost, LifeComment
from django_summernote.widgets import SummernoteWidget

class LifePostForm(forms.ModelForm):
    class Meta:
        model = LifePost
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

class LifeAdminPostForm(forms.ModelForm):
    class Meta:
        model = LifePost
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

class LifeCommentForm(forms.ModelForm):
    class Meta:
        model = LifeComment
        fields = ('text',)