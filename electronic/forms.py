from django import forms
from .models import ElectronicPost,ElectronicComment
from django_summernote.widgets import SummernoteWidget

class ElectronicPostForm(forms.ModelForm):
    class Meta:
        model = ElectronicPost
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

class ElectronicAdminPostForm(forms.ModelForm):
    class Meta:
        model = ElectronicPost
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

class ElectronicCommentForm(forms.ModelForm):
    class Meta:
        model = ElectronicComment
        fields = ('text',)