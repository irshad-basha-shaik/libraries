from django.db import models
from django.views import generic

class Book(models.Model):
    ISBN=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    edition=models.IntegerField(default='1000')
    publication=models.CharField(max_length=100)
    price=models.IntegerField(default=10 )

class Meta:
    db_table="book"
