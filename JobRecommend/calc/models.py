from __future__ import unicode_literals
from django.db import models


class Goods(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sales = models.IntegerField()
    stock = models.IntegerField()
    detail = models.CharField(max_length=255)

    def __str__(self):
        return self.id + self.name + self.price + self.sales + self.stock + self.detail
