from django.contrib.auth.forms import UserCreationForm #for sign up form
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #for success or error msg
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] #for regular user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('There was an error, try again!'))
            return redirect("login")
    else:
        return render(request, 'authenticate/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ('You were logged out!'))
    return redirect('/')
    
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1'] #for regular user
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('Successfully Signed Up!'))
            return redirect('/')
        
    else:
        form = UserCreationForm
        
    return render(request, 'authenticate/signup.html', {'form':form,})