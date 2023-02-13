from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    username =''
    if request.user.is_authenticated:
        username=request.user
       
    context = {'username':username}
    return render(request, 'index.html', context)



def signup(request):
    message = ''
    if request.user.is_authenticated:
            return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            try:
                if password1 != password2:
                    message='The entered passwords do not match'
                elif username.isalnum() == False:
                    message='Please enter alphanumeric number'
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    return redirect('signin')
            #If it can't create the user -> the username is already in the database
            except:
                message = 'Username is already taken'
            
    context={'message':message}

    return render(request, 'signup.html', context)



def signin(request):
    message = ''
    #If already logged in
    if request.user.is_authenticated:
        return redirect('home')
    #If not already logged in --> about to log in
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password1 = request.POST['password1']


            user = authenticate(username=username, password=password1)

            #if the entered user exists in the database
            if user is not None:
                login(request, user)
                return redirect('home')
            #if the entered user doesnt exist in the database
            else:
                message = 'User is not authenticated'
            
        
    context={'message':message}
    return render(request, 'signin.html', context)



def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')