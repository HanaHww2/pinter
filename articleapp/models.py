from django.contrib.auth.models import User
from django.db import models
from projectapp.models import Project


# Create your models here.
class Article(models.Model):
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, related_name='article' )
    writer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='article')
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_created=True, null=True)