from django.shortcuts import render
from mysite.settings import BASE_DIR


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')

def account(request):
    return render(request, 'account.html')
