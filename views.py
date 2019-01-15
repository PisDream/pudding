from django.shortcuts import render


def index(request):
    return render(request,'index.html',{'a':30})


def login(request):
    return render(request,'login.html')
