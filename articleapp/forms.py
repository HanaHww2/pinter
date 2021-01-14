from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreateForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable',
                                                           'style':'min-height: 10rem; heigth:auto;'+
                                                                   'text-align:left;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['project', 'title', 'image', 'content']
