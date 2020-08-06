from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):

    if request.method =='post':
        name=request.post['name']
        email=request.post['email']
        date=request.post['date']
        investigation=request.post['investigation']
        history=request.post['history']
        password=request.post['password']

        user=User.objects.create_user(username=name,password=password,email=email,date=date,history=history,investigation=investigation)
        user.save()

        print('user created')

        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    return render(request,'login.html')