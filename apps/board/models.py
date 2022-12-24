from django.db import models
from apps.workspace.models import Workspace
import uuid
# Create your models here.
# faltan los modelos UserWorkSpaces Y user cards

class Board(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False)
    description = models.TextField(max_length=200,null=False,blank=False)
    workspace = models.ForeignKey(Workspace,on_delete=models.CASCADE)
    uid = models.CharField(default = str(uuid.uuid4())[:8],max_length=8,blank=True,null=True)

class Column(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False)
    board = models.ForeignKey(Board,on_delete=models.CASCADE)

class Card(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False)
    description = models.TextField(max_length=200,null=True,blank=True)
    deadline_date = models.DateField(blank=True,null=True)
    column = models.ForeignKey(Column,on_delete=models.CASCADE)

class ImageCard(models.Model):
    image = models.ImageField(upload_to='media/image_card')
    card = models.ForeignKey(Card,on_delete=models.CASCADE)

class Tag(models.Model):
    name_tag = models.CharField(max_length=30)
    color_tag = models.CharField(max_length=30)

class TagCard(models.Model):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    card = models.ForeignKey(Card,on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/comment')
