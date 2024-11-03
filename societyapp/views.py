from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login  ")
        return redirect('/auth/login')
    
    return render(request,'index.html')