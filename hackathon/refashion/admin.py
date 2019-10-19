from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from refashion.models import User, Customer, Retailer, RewardRate

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Retailer)
admin.site.register(RewardRate)