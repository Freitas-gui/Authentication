from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, SignUpFormPsi
from django.contrib.auth.models import User
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profileperson.birth_date = form.cleaned_data.get('birth_date')
            user.profileperson.first_name = form.cleaned_data.get('first_name')
            user.profileperson.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('url_authentication')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})

def update_profile(request):
    if request.method == 'POST':
        psi_form = SignUpFormPsi(request.POST, instance=request.user)
        if psi_form.is_valid():
            user = psi_form.save()
            user.refresh_from_db() # load the profile instance created by the signal
            user.profileperson.bio = psi_form.cleaned_data.get('bio')
            user.profileperson.crp = psi_form.cleaned_data.get('crp')
            user.save()
            user = authenticate(username=user.username, password=user.password)
            login(request, user)
            return redirect('url_psi_confirmado')
        else:
            messages.error(request,('Please correct the error below.'))
    else:
        psi_form = SignUpFormPsi(instance=request.user)
    return render(request, 'authentication/signup_psi.html', {'psi_form': psi_form})

def psi_confirmado(request):
    return render(request , 'authentication/psi_confirmado.html')


def authentication(request):
    return render(request , 'authentication/authentication.html')

def my_logout(request):
    logout(request)
    return redirect('url_authentication')