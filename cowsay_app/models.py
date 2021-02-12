# https://stackoverflow.com/questions/34147353/python-subprocess-chaining-commands-with-subprocess-run?rq=1
from django.db import models
# Create your models here.
class Cowsay(models.Model):
    # pycharm added line below
    # objects = None
    # use CharField when you need to limit the maximum length, TextField otherwise
    cowsay_string = models.TextField()

    def __str__(self):
        return self.cowsay_string

