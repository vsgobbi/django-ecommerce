from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as translate
from .forms import UserRegisterForm, SignIn
from .forms import AddressRegisterForm
from django.contrib.auth import views as auth_views


def login(request):
    return render(request, "register/login.html")


def form_login(request):
    if request.method == "POST":
        form = SignIn(request.POST)
    else:
        form = UserRegisterForm()
        render(request, "register/signup.html", {"form": form})
    return render(request, "register/login.html", {"form": form})


def register_user(request):

    if request.method and request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.objects.create(user=user)
            messages.success(request, translate("Conta criada com sucesso!"))
            return render(request, "register/registered.html", {"user": user})

    else:
        form = UserRegisterForm()

    return render(request, "register/signup.html", {"form": form})


def register_address(request):

    if request.method and request.method == "POST":
        form = AddressRegisterForm(request.POST)
        if form.is_valid():
            address = form.save()
            return render(request, "register/createdaddress.html", {"address": address})

    else:
        form = AddressRegisterForm()

    return render(request, "register/address.html", {"form": form})


def logout(request):
    auth_views.LogoutView.as_view()
    request.user = "None"
    if not request.user:
        return redirect("/")

    return render(request, 'register/logged_out.html')
