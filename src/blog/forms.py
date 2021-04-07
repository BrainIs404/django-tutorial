from django import forms

from .models import Article

""" class articleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder" : "your title"}
        
        ))
    author = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder" : "your title"}
        
        )
    )

    date = forms.DateTimeInput()
    text = forms.TextInput() """

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'author',
            'date',
            'text',
        ]