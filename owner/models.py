from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.brand_name


class Mobile(models.Model):
    mobile_name=models.CharField(max_length=100,unique=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    price=models.IntegerField(blank=False)
    memory=models.CharField(max_length=120)
    os=models.CharField(max_length=120)
    specs=models.CharField(max_length=120)
    image=models.ImageField(upload_to="images")

    def __str__(self):
        return self.mobile_name