import imp
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from crop_budget.forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from crop_budget.decorators import unauthenticated_user
# Create your views here.
@unauthenticated_user()
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
    else:
        form = CustomUserCreationForm()
        context = {
        'form':form,
        }
        return render(request,'crop_budget/register.html',context)
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request,'crop_budget/home.html')

@login_required
def crop(request):
    return render(request,'crop_budget/crop.html')