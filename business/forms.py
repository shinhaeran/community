from django import forms
from .models import BusinessPost,BusinessComment
from django_summernote.widgets import SummernoteWidget

class BusinessPostForm(forms.ModelForm):
    class Meta:
        model = BusinessPost
        fields = ('title', 'content',)
    
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

class BusinessAdminPostForm(forms.ModelForm):
    class Meta:
        model = BusinessPost
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

class BusinessCommentForm(forms.ModelForm):
    class Meta:
        model = BusinessComment
        fields = ('text',)