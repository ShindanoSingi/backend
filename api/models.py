import datetime
from distutils.command.upload import upload
from email.mime import image
from urllib.parse import MAX_CACHE_SIZE
from django.db import models
import datetime

from traitlets import default


# Create your models here.
class Product(models.Model):
    item = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(
        upload_to='images/', height_field=None, width_field=None, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    countryOfOrigin = models.CharField(max_length=200, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item


class Expense(models.Model):
    item = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item


class Revenue(models.Model):
    item = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item
