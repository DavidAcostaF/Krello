from django.db import models
from apps.workspace.models import Workspace
# Create your models here.

class UserType(models.Model):
    user_type = models.CharField(max_length=30)

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    first_surname = models.CharField(max_length=20)
    second_surname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    img_profile = models.ImageField(upload_to='media/img_profile')
    birthdate = models.CharField(max_length=20)
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE)

class UsersWorkspaces(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace,on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE)