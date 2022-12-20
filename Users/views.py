from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User 


def SignUp(request):
 
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            password1 = request.POST['password1']


            if password == password1:
                
                try:
                        User.objects.create_user(username=email, password=password)
                        user = authenticate(username=email, password=password)           
                        login(request, user)
                        return redirect('home')
                except:
                        messages.warning(request, 'Existing user')


            else:
                messages.warning(request, 'Passwords do not match')

        return render(request, 'account/sign-up.html', {} )

    

def Logout(request):

    logout(request)
    return redirect('home')


