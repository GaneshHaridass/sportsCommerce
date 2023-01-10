from django.db import models
from django.contrib.auth.models import User
# from PIL import Image


class CustomerApplicantTable(models.Model):
    username=models.CharField(max_length=20,unique=True)
    email=models.EmailField(max_length=20)
    contact_no=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    addresss=models.TextField(max_length=200,null=True,blank=True)
    def __str__(self):  
        return self.username 



class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
class Tags(models.Model):
    tag_name=models.CharField(max_length=200)
    def __str__(self):
        return self.tag_name

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    digital=models.BooleanField(default=False,null=True,blank=False)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    tags=models.ManyToManyField(Tags)
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(blank=True,auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transcation_id = models.CharField(max_length=200,null=True)
    def __str__(self):
        return (self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(blank=True,auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    address=models.CharField(max_length=200,null=False)
    city = models.CharField(max_length=200,null=False)
    state = models.CharField(max_length=200,null=False)
    zipcode = models.DateTimeField(blank=True)

    def __str__(self):
        return self.address
