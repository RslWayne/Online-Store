from django.contrib.auth.models import User
from django.db import models
from datetime import date

# Create your models here
class Product(models.Model):
    choise = (
        ('RPhone', 'RPhone'),
        ('Razer', 'Razer'),
        ('Rpods', 'Rpods'),
        ('Mouse', 'Mouse')
    )
    image = models.ImageField(blank=True,null=True,default='default_product_image.png')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    type = models.CharField(choices=choise, max_length=50)
    price = models.IntegerField()
    sale = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} {self.type} {self.price}"




class Order(models.Model):
    statuses = (
        ('In Process','In Process'),
        ('Delivered','Delivered'),
        ('Not Delivered','Not Delivered')
    )
    p_methods = (
        ('money','money'),
        ('wallet','wallet')
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20,choices=statuses,default='In Process')
    date_created = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20,choices=p_methods)

class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

class Contacts(models.Model):
    type = ()
    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    latitude = models.CharField(max_length=150)


class Profile(models.Model):
    gender = (
        ('F','F'),
        ('M','M')

    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='image_suit.jpeg',blank=True)
    full_name = models.CharField(max_length=50)
    gender = models.CharField(choices=gender,max_length=20)
    description = models.TextField()
    birth_date = models.DateField(default=date.today())
    twitter_link = models.CharField(max_length=50)
    wallet = models.PositiveIntegerField(default=0)
    order_count = models.PositiveIntegerField(default=0)

