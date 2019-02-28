from django import forms
from .models import EngineerPost,EngineerComment
from django_summernote.widgets import SummernoteWidget

class EngineerPostForm(forms.ModelForm):
    class Meta:
        model = EngineerPost
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
    
class EngineerAdminPostForm(forms.ModelForm):
    class Meta:
        model = EngineerPost
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

class EngineerCommentForm(forms.ModelForm):
    class Meta:
        model = EngineerComment
        fields = ('text',)