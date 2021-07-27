from django.db import models

from django.db import models

class ProductModel(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    photo = models.ImageField()
