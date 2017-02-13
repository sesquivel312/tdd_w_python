from django.db import models

# Create your models here.


class List(models.Model):
    """
    List table is a list of list names
    """
    pass


class Item(models.Model):
    """
    Item table contains all items on lists, each instance/row points to the list of which it is a member
    """
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
