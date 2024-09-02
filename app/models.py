from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phoneno=models.CharField(max_length=10)
    desc=models.TextField()

    def __str__(self):
        return self.email


class Medicines(models.Model):
    medicine_name=models.CharField(max_length=250)
    medicine_image=models.ImageField(upload_to="products",blank=True,null=True)
    medicine_price=models.IntegerField()
    medicine_descripton=models.TextField()
    medicine_exp=models.DateField()
    def __str__(self):
        return self.medicine_name

class ProductItems(models.Model):
    prod_name=models.CharField(max_length=250)
    prod_image=models.ImageField(upload_to="products",blank=True,null=True)
    prod_price=models.IntegerField()
    prod_descripton=models.TextField()
    prod_exp=models.DateField()
    def __str__(self):
        return self.prod_name

class MyOrders(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    items=models.CharField(max_length=1500)
    address=models.TextField()
    quantity=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    phone_num=models.CharField(max_length=10)
    delivery=models.BooleanField(default=False)
    location = models.CharField(max_length=100, default='Unknown')
    def __int__(self):
        return self.id
class Sell(models.Model):
    sell_category=models.CharField(max_length=250)
    sell_name=models.CharField(max_length=250)
    sell_image=models.ImageField(upload_to="products",blank=True,null=True)
    sell_price=models.IntegerField()
    sell_description = models.TextField()
    sell_location = models.CharField(max_length=100, default='Unknown')
    sell_by=models.CharField(max_length=100, default='Unknown')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.sell_name
class FarmerProfile(models.Model):
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    location = models.CharField(max_length=100, default='Unknown') 
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class customerProfile(models.Model):
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    location = models.CharField(max_length=100, default='Unknown')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.username