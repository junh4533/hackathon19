from django.db import models
from django.contrib.auth.models import Group, User, Permission
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, UserManager
from datetime import datetime, time, date
import random
import uuid
# Create your models here.

class User(AbstractUser):
    users = (
        ('customer', 'Customer'),
        ('retailer', 'Retailer'),
    )

    user_type = models.CharField(choices=users, max_length=8)

    #return the users' name
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name) 

class Address(models.Model):
    address_id = models.AutoField(unique=True, primary_key=True)
    street = models.CharField(max_length=150, blank=False)
    city = models.CharField(max_length=150, blank=False)
    state = models.CharField(max_length=150, blank=False)
    zip_code = models.PositiveSmallIntegerField(blank=False)

    #return street as a string
    def __str__(self):
        return str(self.street)

class Customer(models.Model): 
    customer_id = models.AutoField(unique=True, primary_key=True)
    customer_number = models.PositiveSmallIntegerField(blank=False, default=random.randint(10000,99999))
    user = models.OneToOneField(User, on_delete=models.CASCADE) #customer id
    user.user_type = "customer"
    address = models.ForeignKey(Address, on_delete=models.CASCADE) #customer address
    points_balance = models.PositiveSmallIntegerField(blank=False, default=0)

    #return the customer's name
    def __str__(self):
        return str(self.user) + " customer_id: " + str(self.customer_id)

class Retailer(models.Model):
    retailer_id = models.AutoField(unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #retailer id
    user.user_type = "retailer"

    #return the retailer's name
    def __str__(self):
        return str(self.user) + " retailer_id: " + str(self.retailer_id)

class Donation(models.Model):
    donation_id = models.AutoField(unique=True, primary_key=True)
    combined_weight = models.PositiveSmallIntegerField(blank=False, default=0)
    points_added = models.PositiveSmallIntegerField(blank=False, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #user id

    #return the donor and his/her id
    def __str__(self):
        return str(self.user) + " donation_id: " + str(self.donation_id)

class Store(models.Model):
    store_id = models.AutoField(unique=True, primary_key=True)
    store_name = models.CharField(max_length=150, blank=False)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE) #retailer's store address

    #return the store name and id
    def __str__(self):
        return str(self.store_name) + " store_id: " + str(self.store_id)

class Redemption(models.Model):
    redemption_id = models.AutoField(unique=True, primary_key=True)
    redemption_date_time = models.DateTimeField(auto_now=True)
    # redemption_date_time.editable = True
    # coupon_code = models.UUIDField(default=uuid.uuid4, editable=False)
    # coupon_code = models.PositiveSmallIntegerField()
    coupon_code = models.PositiveSmallIntegerField(blank=False)
    # store = models.ForeignKey(Store, on_delete=models.CASCADE) #store
    user = models.ForeignKey(User, on_delete=models.CASCADE) #user id

    #return the redeemer and store
    def __str__(self):
        return str(self.user) + str(self.coupon_code)



# class RewardRate(models.Model):
#     reward_rate_id = models.AutoField(unique=True, primary_key=True)
#     donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    
#     # reward_multiplier = models.DecimalField(default=1, max_digits=7, decimal_places=5)
#     # discount_rate = reward_multiplier * donation.combined_weight
#     # test = models.CharField(max_length=150, blank=False)

#     #return the store name and id
#     def __str__(self):
#         return str(self.store_name, self.store_id)
