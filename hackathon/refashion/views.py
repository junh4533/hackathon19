from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'refashion/index.html')

def rewards(request):
    return render(request, 'refashion/rewards.html')

def profile(request):
    return render(request, 'refashion/profile.html')

def stores(request):
    return render(request, 'refashion/stores.html')