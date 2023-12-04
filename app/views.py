from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from app.forms import SignUpForm


# Create your views here.
def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authentication
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"You have been logged in {username} !")
            return render(request, 'home.html', {'name': username})
        else:
            messages.error(request, "There was an error logging in, please again")
            return redirect('home')
    else:
        return render(request, 'home.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out  !")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully register ! Welcome 😊")
            return redirect('home')
    else:
        form = SignUpForm
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})
