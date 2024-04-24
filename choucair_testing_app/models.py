from django.db import models

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=50, blank=False)
    price = models.IntegerField(blank=False)
    stock = models.IntegerField(blank=False)
    product_image = models.ImageField(blank=False, upload_to="product image/", default="")
    create_date = models.DateField(blank=True)
    update_date = models.DateField(blank=True, null=True)
