from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from refashion.models import User, Customer, Retailer, Store, Donation, Address, Redemption

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Retailer)
admin.site.register(Store)
admin.site.register(Donation)
admin.site.register(Address)

# class Redemption(admin.ModelAdmin):
#     readonly_fields = ('redemption_date_time','coupon_code')

# admin.site.register(Redemption, RedemptionAdmin)
admin.site.register(Redemption)