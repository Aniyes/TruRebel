from django.db import models
from django import forms

# Create your models here.



class Product(models.Model,):

    Sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    title = models.CharField(max_length=30)
    description = models.TextField()
    size = models.CharField(max_length=1, choices=Sizes, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=6.99, null=True, blank=True)
    photo = models.ImageField(upload_to='product')
   # collection = Product.objects.all()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Register(models.Model):

    User_name = models.CharField(max_length=15)
    Password = models.CharField(max_length=15)
    Email = models.CharField(max_length=20)

