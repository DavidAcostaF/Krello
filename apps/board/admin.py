from django.contrib import admin
from apps.board import models
# Register your models here.

admin.site.register(models.Board)
admin.site.register(models.Column)
admin.site.register(models.Card)