from django.shortcuts import render, redirect
from django.contrib.auth import logout

def authentication(request):
    return render(request , 'authentication/authentication.html')

def my_logout(request):
    logout(request)
    return redirect('url_authentication')