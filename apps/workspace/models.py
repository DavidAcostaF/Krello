from django.db import models

# Create your models here.

class Workspace(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False)
    description = models.TextField(max_length=200,null=False,blank=False)