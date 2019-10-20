from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('retailer/',views.retailer, name='retailer'), #retailer page
    path('home/',views.customer, name='customer'), #home page for customers
    path('stores/',views.stores, name='stores'), #stores page
    path('redeem/',views.redeem, name='redeem'), #redeem page
    path('rewards/',views.rewards, name='rewards'), #rewards page
]