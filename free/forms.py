from django import forms
from .models import FreePost, FreeComment
from django_summernote.widgets import SummernoteWidget

class FreePostForm(forms.ModelForm):
    class Meta:
        model = FreePost
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

class FreeAdminPostForm(forms.ModelForm):
    class Meta:
        model = FreePost
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

class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields = ('text',)