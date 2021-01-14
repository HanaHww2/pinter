from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from commentapp.forms import CommentCreateForm
from projectapp.decorators import project_authenticated_required
from projectapp.forms import ProjectCreateForm
from projectapp.models import Project
from subscribeapp.models import Subscribe


@method_decorator(login_required, 'post')
@method_decorator(login_required, 'get')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projectapp/create.html'

    # def form_valid(self, form):
    #     temp_project = form.save(commit=False)
    #     temp_project.admin = self.request.user
    #     temp_project.save()
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

# @method_decorator(project_authenticated_required, 'post')
# @method_decorator(project_authenticated_required, 'get')
# class ArticleUpdateView(UpdateView):
#     model = Project
#     context_object_name = 'target_article'
#     form_class = ArticleCreateForm
#     template_name = 'articleapp/update.html'
#
#     def get_success_url(self):
#         return reverse('articleapp:detail', kwargs={'pk':self.object.pk})

@method_decorator(project_authenticated_required, 'post')
@method_decorator(project_authenticated_required, 'get')
class ProjectDeleteView(DeleteView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/delete.html'
    success_url = reverse_lazy('projectapp:list')

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 12 # 16

class ProjectDetailView(DetailView, MultipleObjectMixin, FormMixin):
    model = Project
    form_class = CommentCreateForm
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    paginate_by = 12 # 16

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscribe = Subscribe.objects.filter(user=user, project=project)

        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscribe=subscribe,
                                                               **kwargs)