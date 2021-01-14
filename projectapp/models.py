from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Project(models.Model):
    # admin = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='article')
    title = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    description = models.CharField(max_length=200, null=True)
    created_date = models.DateField(auto_created=True, null=True)

    def __str__(self):
        return f'{self.title}' # {self.pk}
