#Author : Jordan Montenegro

from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




# Create your models here.
class RegularPizza(models.Model):
	name = models.CharField(max_length=64)
	smallprice = models.DecimalField(max_digits=4, decimal_places=2)
	largeprice = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} (small = {self.smallprice}, large = {self.largeprice})"


class SicilianPizza(models.Model):
	name = models.CharField(max_length=64)
	smallprice = models.DecimalField(max_digits=4, decimal_places=2)
	largeprice = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return f"{self.name} (small = {self.smallprice}, large = {self.largeprice})"
	
class DinnerPlatters(models.Model):
	name = models.CharField(max_length=64)
	smallprice = models.DecimalField(max_digits=4, decimal_places=2)
	largeprice = models.DecimalField(max_digits=4, decimal_places=2)
	def __str__(self):
		return f"{self.name} (small = {self.smallprice}, large = {self.largeprice})"


class Toppings(models.Model):
	name = models.CharField(max_length=64)
	def __str__(self):
		return f"{self.name}"

class Subs(models.Model):
	name = models.CharField(max_length=64)
	smallprice = models.DecimalField(max_digits=4, decimal_places=2)
	largeprice = models.DecimalField(max_digits=4, decimal_places=2)
	def __str__(self):
		return f"{self.name} (small = {self.smallprice}, large = {self.largeprice})"
		
class Salads(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	def __str__(self):
		return f"{self.name} (price = {self.price})"
		
class Pasta(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	def __str__(self):
		return f"{self.name} (price = {self.price})" 
		
class Order(models.Model):
	username = models.CharField(max_length=64)
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	#total = models.DecimalField(max_digits=4, decimal_places=2)
	
	def __str__(self):
		return f"{self.username}: {self.name}({self.price})"

class Confirmed_order(models.Model):
	username = models.CharField(max_length=64)
	orders = models.CharField (max_length=1000)
	total = models.CharField(max_length=64)
	completed=models.BooleanField(default=False)
	
	def __str__(self):
		if self.completed:
			return f"{self.username} : {self.orders} {self.total} Completed"
		else :
			return f"{self.username} : {self.orders} {self.total} Pending"
