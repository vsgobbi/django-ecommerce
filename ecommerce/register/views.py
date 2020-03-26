from django.shortcuts import render
from .forms import RegisterForm


def register_user(request):

    if request.method and request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            return
    else:
        form = RegisterForm()

    return render(request, "register/signup.html", {'form': form})
