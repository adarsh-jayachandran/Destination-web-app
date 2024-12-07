from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from Travel.models import Destination
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        passowrd2 = request.POST['password2']
        email = request.POST['email']

        if password1 == passowrd2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def destination_detail(request, id):
    dest = get_object_or_404(Destination,id=id)
    template_name = f"{dest.name.lower()}.html"
  
    return render(request,template_name,{'dest':dest})