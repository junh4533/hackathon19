from django.db import models
from django.contrib.auth.models import Group, User, Permission
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, UserManager
from datetime import datetime, time, date
# Create your models here.

class User(AbstractUser):
    users = (
        ('customer', 'Customer'),
        ('retailer', 'Retailer'),
    )

    user_type = models.CharField(choices=users, max_length=8)

    #return the users' name
    def __str__(self):
        return self.first_name + " " + self.last_name

class Address(models.Model):
    address_id = models.AutoField(unique=True, primary_key=True)
    street = models.CharField(max_length=150, blank=False)
    city = models.CharField(max_length=150, blank=False)
    state = models.CharField(max_length=150, blank=False)
    zip_code = models.PositiveSmallIntegerField(blank=False)

class Customer(models.Model):
    customer_id = models.AutoField(unique=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE) #customer id
    user.user_type = "customer"
    address = models.ForeignKey(Address, on_delete=models.CASCADE) #customer address

class Retailer(models.Model):
    retailer_id = models.AutoField(unique=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE) #retailer id
    user.user_type = "retailer"

class Donation(models.Model):
    donation_id = models.AutoField(unique=True, primary_key=True)
    combined_weight = models.PositiveSmallIntegerField(blank=False)

class Redemption(models.Model):
    redemption_id = models.AutoField(unique=True, primary_key=True)
    redemption_date_time = models.DateTimeField(auto_now=True)

class Store(models.Model):
    store_id = models.AutoField(unique=True, primary_key=True)
    store_name = models.CharField(max_length=150, blank=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE) #retailer address

class RewardRate(models.Model):
    reward_rate_id = models.AutoField(unique=True, primary_key=True)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    reward_multiplier = models.DecimalField(default=1, max_digits=7, decimal_places=5)
    # discount_rate = reward_multiplier * donation.combined_weight
    coupon_code = models.CharField(max_length=150, blank=False)
    test = models.CharField(max_length=150, blank=False)
