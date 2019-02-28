from django import forms
from .models import HumanPost, HumanComment
from django_summernote.widgets import SummernoteWidget

class HumanPostForm(forms.ModelForm):
    class Meta:
        model = HumanPost
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

class HumanAdminPostForm(forms.ModelForm):
    class Meta:
        model = HumanPost
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

class HumanCommentForm(forms.ModelForm):
    class Meta:
        model = HumanComment
        fields = ('text',)