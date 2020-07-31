from django.shortcuts import render

def loginPage(request):
    return render(request, 'login.html')

def signUpPage(request):
    return render(request, 'signUp.html')