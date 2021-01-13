from django.http import HttpResponseForbidden

from articleapp.models import Article
from projectapp.models import Project


def project_authenticated_required(func):
    def decorated(request, *args, **kwargs):
        project = Project.objects.get(pk=kwargs['pk'])
        if not project.admin == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
