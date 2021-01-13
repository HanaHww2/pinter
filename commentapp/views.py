from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_authenticated_required
from commentapp.forms import CommentCreateForm
from commentapp.models import Comment
from projectapp.models import Project

# Create your views here.
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)

        if self.request.POST['project_pk']:
            temp_comment.project = Project.objects.get(pk=self.request.POST['project_pk'])
        elif self.request.POST['article_pk']:
            temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        if self.object.article:
            return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
        elif self.object.project:
            return reverse('projectapp:detail', kwargs={'pk': self.object.project.pk})


@method_decorator(comment_authenticated_required, 'get')
@method_decorator(comment_authenticated_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        if self.object.article:
            return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
        elif self.object.project:
            return reverse('projectapp:detail', kwargs={'pk': self.object.project.pk})
