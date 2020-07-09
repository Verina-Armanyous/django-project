from django.db import models
from django.conf import settings

# Create your models here.


# list of things that people can donate for
class Item(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    def __str__(self):
        return self.title


# shopping cart
class Order(models.Model):
    def __str__(self):
        return self.title
