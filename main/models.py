from django.db import models
from django.contrib import auth
from django.utils.timezone import now
from django.dispatch import receiver

# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text



class Topic(models.Model):
    title = models.CharField(max_length=150, unique=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    search_string = models.TextField(max_length=1000, blank=True, null=True)
    asset_description = models.TextField(max_length=1000, blank=True, null=True)
    #contributedyby = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE, verbose_name="Author")

    def __str__(self):
        return self.title