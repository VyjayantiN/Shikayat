from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    return render(request,'citizen/home.html')
def about(request):
    return render(request,'citizen/about.html')
def otp(request):
    return render(request,'citizen/otp.html')