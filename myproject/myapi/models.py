from django.db import models

# Create your models here.

class Item(models.Model):
    category=models.CharField(max_length=20)
    subcategory=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.name 

class Doctor(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    title=models.CharField(max_length=40,blank=True,null=True)
    department=models.CharField(max_length=40,blank=True,null=True)
    image= models.ImageField(upload_to='doctor_images/', null=True, blank=True)
    