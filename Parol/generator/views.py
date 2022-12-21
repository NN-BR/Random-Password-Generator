from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html', {'egman':'Black eggs', 'password':'Lulz'})

def password(request):

    char = list("abcdefghijklmnopqstuvwxyz")

    if request.GET.get('uppercase'):
        char.extend(list("ABCDEFGHIJKLMNOPQSTUVWXYZ"))

    if request.GET.get('special'):
        char.extend(list("!@#$%^&*(_)+=-/*~"))

    if request.GET.get('numbers'):
        char.extend(list("1234567890"))

    lenght = int(request.GET.get('lenght pass', 8))

    thepassword = " "

    for x in range(lenght):
        thepassword += random.choice(char)
    return render(request, 'generator/password.html', {'password':thepassword})

def infor(request):
    return  render(request, 'generator/info.html')