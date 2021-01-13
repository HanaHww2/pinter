from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article
from projectapp.models import Project


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name='comment')
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')

    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)