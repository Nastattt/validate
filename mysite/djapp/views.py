from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


def reg(request):
    registration_form = Registration_form()
    return render(request, "index.html", {"form": registration_form})


def congrats(request):
    if request.method == "POST":
        registration_form = Registration_form(request.POST)
        if registration_form.is_valid():
            name = registration_form.cleaned_data['name']
            email = registration_form.cleaned_data['email']
            password = registration_form.cleaned_data['password']
            return HttpResponse(
                f'{name}, поздравляю с регистрацией!<br>Указанные вами данные: Name - {name}, Email - {email}, Password - {password}')
        else:
            return redirect("reg")
    else:
        return redirect("reg")


def sign_in(request):
    signin = Sign_in_form()
    return render(request, "sign_in.html", {"signin": signin})


def successful(request):
    if request.method == "POST":
        signin = Sign_in_form(request.POST)
        name = request.POST.get('name')
        password = request.POST.get('password')
        if signin.is_valid() and name == 'User1' and password == '12345678':
            return HttpResponse("Поздравляю с успешным входом")
        else:
            return redirect("reg")
    else:
        return redirect("reg")


def forget(request):
    return HttpResponse("Забыли пароль? Обратитесь в службу поддержки")
