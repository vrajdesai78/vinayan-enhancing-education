from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email,password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/login')
    else:
        return render(request,'login.html')
        
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        phone = request.POST['phone']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        user_type = request.POST['user_type']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2: 
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already registered')
                return redirect('accounts/register')
            else:
                user = User.objects.create_user(email=email, password=password1, date_of_birth=date_of_birth,user_type=user_type, first_name=first_name, last_name=last_name, phone=phone)
                user.save()
                messages.info(request,'Created User')
                return redirect('/accounts/login')
        else:
            messages.info(request,'Password is not matching')
            return redirect('accounts/register')
        return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')