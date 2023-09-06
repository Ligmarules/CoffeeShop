from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Coffee
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from coffee.models import Coffee
from django.http import JsonResponse
import json

#@login_required(login_url='login')



def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})

def about(request):
    coffee = Coffee.objects.all()
    return render(request, 'about.html', {'coffee': coffee})

def help(request):
    coffee = Coffee.objects.all()
    return render(request, 'help.html', {'coffee': coffee})

def add(request):
    coffee = Coffee.objects.all()
    return render(request, 'add.html', {'coffee': coffee})

def Signup(request):
    form = SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("user does not exist")
    else:
        return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect ('login')


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)     
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']         
            html = render_to_string('emails/contactform.html', {'name': name, 'email': email, 'content': content})
            print('The Form was valid')          
            send_mail('The contact form subject', 'This is the message', 'noreply@codewithstein.com', ['codewithtestein@gmail.com'], html_message=html)          
            return redirect('index')
    else:
        form = ContactForm()  
    return render(request, 'help.html', {'form': form})
