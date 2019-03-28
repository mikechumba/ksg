from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):

   class Meta:
      model = User
      fields = UserCreationForm.Meta.fields + ('first_name','last_name','username','email','password1')

class LoginForm(AuthenticationForm):
   '''
   To handle user login
   '''

   class Meta:
      model = User
      fields = ['username','password'] 