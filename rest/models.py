from django.db import models

# Create your models here.

class Product(models.Model):
    product_url = models.TextField()
    product_url_created_at = models.DateField()
    consult_date = models.DateField()
    c = models.IntegerField() #total de vendas