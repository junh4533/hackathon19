from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate

# models
from refashion.models import *
from django.contrib.auth.models import User

# forms
from django.contrib.auth import update_session_auth_hash
from refashion.forms import * #import all forms

import random

def customer(request):
    if request.method == 'GET':
        user = Customer.objects.get(customer_id=request.user.customer.customer_id).customer_number
        args ={
            "user":user,
        }
    return render(request, 'refashion/index.html',args)

def retailer(request):
    if request.method == 'POST':
        form = DonateForm(request.POST)
        if form.is_valid():
            print("valid form")
            form.save()
            points_to_add = form.cleaned_data['combined_weight']*10 #get 10 points for every ounce donated
            balance = Customer.objects.get(customer_id=request.user.customer.customer_id).points_balance
            Customer.objects.filter(customer_id=request.user.customer.customer_id).update(points_balance=balance+points_to_add) #add specified points to the selected user
            form = DonateForm
            success = "Successfully added points"
            args = {'success':success, "form":form}
            return render(request, 'refashion/retailer.html', args)
        else:
            failed = "Unable to add points"
            args = {'failed':failed, "form":form}
            return render(request, 'refashion/retailer.html', args)
    else:
        if request.user.user_type == "customer":
            return redirect('customer') 
        form = DonateForm
        args = {'form':form}
        return render(request, 'refashion/retailer.html',args)

def rewards(request):
    if request.method == 'GET':
        redemption = Redemption.objects.filter(user=request.user).values_list('coupon_code', flat=True)
        # redemption = Redemption.objects.filter(user=request.user)
        print(redemption)
        print(request.user)
        args ={
            "redemption":redemption,
        }
        return render(request, 'refashion/rewards.html',args)
        

def redeem(request):
    if request.method == 'GET':
        balance = Customer.objects.get(customer_id=request.user.customer.customer_id).points_balance
        args ={
            "balance":balance,
        }
        return render(request, 'refashion/redeem.html', args)     
    elif request.method == 'POST':
        balance = Customer.objects.get(customer_id=request.user.customer.customer_id).points_balance
        Customer.objects.filter(customer_id=request.user.customer.customer_id).update(points_balance=balance-100) #subtract 100 points to redeem coupon
        Redemption.objects.create(user=request.user,coupon_code=random.randint(10000000,99999999))
        success = "redeemed 100 points"
        args = {'success':success}
        # return render(request, 'refashion/rewards.html', args)
        # return rewards(request)
        return redirect('rewards')
        # return render(request, '../rewards', args)    


def profile(request):
    return render(request, 'refashion/profile.html')

def stores(request):
    # if request.method == 'GET':
    #     user = Customer.objects.get(customer_id=request.user.customer.customer_id).customer_number
    #     args ={
    #         "user":user,
    #     }
    # if request.method == 'POST':
    return render(request, 'refashion/stores.html')