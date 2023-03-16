from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



def home(requests):
    return render (requests, "index.html")













#The compoents page 
def community(requests):
    return render (requests, "components/community.html")

def howto(requests):
    return render (requests, "components/howto.html")

def information(requests):
    return render (requests, "components/information.html")

def services(requests):
    return render (requests, "components/services.html")


def studentlife(requests):
    return render (requests, "components/studentlife.html")














#The Authenication Process


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})






def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('username', 'Invalid username or password.')
                form.add_error('password', 'Invalid username or password.')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'auth/login.html', context)




def logout_view(request):
     logout(request)
     return redirect('home') 