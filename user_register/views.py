from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        user = UserRegisterForm(request.POST)
        if user.is_valid():
            if User.objects.filter(email=user.cleaned_data.get('email')).exists():
                messages.error(request, "Email already exists")
            else:
                user.save()
                messages.success(request, "User Registered Successfully...")
        else:
            messages.error(request, user.errors)
    
    form = UserRegisterForm()
    return render(request, 'user_register/register.html', {'form': form})