from django import forms
from .models import AgriculturePost, AgricultureComment
from django_summernote.widgets import SummernoteWidget

class AgriculturePostForm(forms.ModelForm):
    class Meta:
        model = AgriculturePost
        fields = ( 'title', 'content',)
    # notice = forms.BooleanField(                #줄맞춤 굉장히 중요
    #     widget=forms.CheckboxInput(attrs={
    #         'class': 'notice-control',
    #         'disabled': True,
    #     })
    # )
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

class AgricultureAdminPostForm(forms.ModelForm):
    class Meta:
        model = AgriculturePost
        fields = ('title', 'content', 'notice')
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
    # notice = forms.BooleanField(
    #     widget = forms.CheckboxInput(attrs={
    #         'class' : 'notice-control',
    #         'disabled' : False,
    #     })
    # )

class AgricultureCommentForm(forms.ModelForm):
    class Meta:
        model = AgricultureComment
        fields = ('text',)