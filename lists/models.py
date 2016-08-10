from django.db import models

# Create your models here.
class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='')
    listx = models.ForeignKey(List, default=None)
