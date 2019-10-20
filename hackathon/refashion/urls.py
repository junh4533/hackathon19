from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.login, name='login'),
    # path('customer/', include(([
    #     path('home',views.customer, name='customer'), #home page
    #     path('stores',views.stores, name='stores'), #stores page
    #     path('rewards',views.rewards, name='rewards') #rewards page
    # ]))),
    path('retailer',views.retailer, name='retailer'), #retailer page

    path('home',views.customer, name='customer'), #home page
    path('stores',views.stores, name='stores'), #stores page
    path('redeem',views.redeem, name='redeem'), #redeem page
    path('rewards',views.rewards, name='rewards'), #rewards page
]