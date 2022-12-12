



from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)

def LoginView(request):
    if request.method =='POST':
     form = AuthenticationForm(data = request.POST)
     if form.is_valid():
         
        user = form.get_user()
        return redirect('frontend:home')
    else:
        form = AuthenticationForm()
        return render(request,'user/login.html',{'form':form})


