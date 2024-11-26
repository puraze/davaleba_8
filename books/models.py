
from django.db import models
class Book(models.Model):
    title = models.CharField()
    description = models.TextField()
    author = models.ManyToOneRel()
    category = models.ManyToManyRel()
    rating = models.IntegerField()


class Category(models.Model):
    name = models.CharField()


class Author(models.Model):
    name = models.CharField()
    
