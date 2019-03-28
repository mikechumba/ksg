from django.urls import path
from .forms import LoginForm
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('',views.landing,name='landing'),
   path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm,extra_context={'title': 'Login'}), name='login'),
   path('logout/', views.logout_view, name='logout'),
]
