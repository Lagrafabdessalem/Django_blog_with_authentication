from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})
# Create your views here.

def login_user(request):
    if request.method == "POST":
        auth = AuthenticationForm(data = request.POST)
        if auth.is_valid():
            login(request, auth.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
    else:
         auth = AuthenticationForm()
    return render(request, "users/login.html", {"auth": auth})


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")


        