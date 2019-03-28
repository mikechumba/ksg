from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .models import *
from .forms import *

# Create your views here.

def landing(request):

   title = 'Kenya Scriptwriters Guild.'

   context =  {
      'title': title
   }

   return render(request,'landing.html',context)

def signup(request,role):

   title = 'KSG | Sign Up'

   if request.method == 'POST':
      form = RegistrationForm()
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = authenticate(username=username,password=raw_password)
         login(request,user)
         role = Role.objects.get(role=role)
         profile = Profile.create_profile(user,role)
         profile.save()

   context = {
      'title': title,
      'form': form,
   }

   return render(request,'registration/register.html',context)

def dashboard(request):

   title = f'{request.user.first_name} {request.user.last_name}'

   context = {
      'title': title
   }

   return render(request,'dashboard.html',context)

def logout_view(request):
   logout(request)
   return redirect('login')