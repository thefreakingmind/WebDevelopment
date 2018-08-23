from django.db import models
from django.utils import timezone


class Products(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    img = models.ImageField()

    def __str__(self):
        return self.name
