# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	Name=models.CharField(max_length=30)
	Description=models.TextField(max_length=50)

	def __str__(self):
		return self.Name
		
			
class Product(models.Model):
	Categories=models.ForeignKey(Category,on_delete=models.CASCADE)
	Name=models.CharField(max_length=20,blank=True )
	Image=models.FileField(upload_to='media/',null=True,blank=True)
	IDorSNO=models.IntegerField(default=0,null=True,blank=True)
	Description=models.TextField(max_length=50,null=True,blank=True)
	Price=models.IntegerField(default=0,null=True,blank=True)
	NumbersAvailable=models.IntegerField(default=0,null=True,blank=True)

	def __str__(self):
		return self.Name



class user_details(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	address=models.TextField(max_length=50)
	phonenumber=models.IntegerField()	
	
	def __str__(self):
			return self.user.username

class Cartmodel(models.Model):
	Cart=models.OneToOneField(Product, on_delete=models.CASCADE)
	quantity=models.IntegerField()

	
class CustomerDetail(models.Model):
	Name=models.CharField(max_length=20,blank=True)
	phonenumber=models.IntegerField(default=0)
	Email=models.CharField(max_length=30,blank=True)
	PermanentAddress=models.TextField(max_length=50)
	TemporaryAddress=models.TextField(max_length=50)
	City=models.CharField(max_length=20,blank=True)
	State=models.CharField(max_length=20,blank=True)
	Landmark=models.CharField(max_length=30,blank=True)
	Pincode=models.IntegerField(default=0)
	
class Cart(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	
	
	def __str__(self):
		return self.User.username

	
class Cartitem(models.Model):
	Cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
	product=models.ManyToManyField(Cartmodel)
