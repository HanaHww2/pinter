from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscribe



# Create your views here.
@method_decorator(login_required, 'get')
class SubscribeView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscribe = Subscribe.objects.filter(user=user, project=project)
        print(subscribe)
        if subscribe.exists():
            subscribe.delete()
        else:
            Subscribe(user=user, project=project).save()
        return super(SubscribeView, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscribeListView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        projects = Subscribe.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list