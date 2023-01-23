import datetime
from distutils.command.upload import upload
from email.mime import image
from urllib.parse import MAX_CACHE_SIZE
from django.db import models
import datetime

from traitlets import default


# Create Todo User
class TodoUser(models.Model):
    username = models.CharField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Todo(models.Model):
    todo_user = models.ForeignKey(
        TodoUser, on_delete=models.CASCADE, null=True)
    todo = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(null=True)
    completed = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo


class Bodaboda(models.Model):
    item = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item


class ExpenseBodaboda(models.Model):
    item = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item


class RevenueBodaboda(models.Model):
    item = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item


class Product(models.Model):
    item = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(
        upload_to='images/', blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    countryOfOrigin = models.CharField(max_length=200, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item


class ExpenseProduct(models.Model):
    item = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item


class RevenueProduct(models.Model):
    item = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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
