from django.db import models
# Create your models here.

class Workspace(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False)
    description = models.TextField(max_length=200,null=False,blank=False)
    created_by = models.ForeignKey("users.User",on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
