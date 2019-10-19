from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'), #index page
    path('profile/',views.profile, name='profile'), #profile page
    path('stores/',views.stores, name='stores'), #stores page
    path('rewards',views.rewards, name='rewards') #rewards page
]