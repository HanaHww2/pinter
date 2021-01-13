from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_authenticated_required
from articleapp.forms import ArticleCreateForm
from articleapp.models import Article
from commentapp.forms import CommentCreateForm


@method_decorator(login_required, 'post')
@method_decorator(login_required, 'get')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})

@method_decorator(article_authenticated_required, 'post')
@method_decorator(article_authenticated_required, 'get')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreateForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})

@method_decorator(article_authenticated_required, 'post')
@method_decorator(article_authenticated_required, 'get')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')

class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreateForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 12 # 16
