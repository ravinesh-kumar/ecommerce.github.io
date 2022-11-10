from django.db import models



class product(models.Model):
    productname =models.CharField(max_length=500)
    category_name=models.CharField(max_length=500)
    price=price=models.CharField(max_length=500)
    detail=models.CharField(max_length=500)
    image=models.ImageField(upload_to = "product_upload/images")
    