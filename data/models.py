from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Parent(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=500, null=True, blank=True)
    lastName = models.CharField(max_length=500, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    city= models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip = models.DecimalField(max_digits=14, decimal_places=0, null=True, blank=True)



class Child(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=500,null=True, blank=True)
    lastName = models.CharField(max_length=500, null=True, blank=True)
    parent=models.ForeignKey(Parent,  on_delete=models.CASCADE)


    