from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreateForm(ModelForm):
    class Meta:
        model = Article
        fields = ['project', 'title', 'image', 'content']
