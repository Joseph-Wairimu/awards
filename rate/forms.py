from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Project,Rating

class RegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model= User
        fields=["username","email","password1","password2"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','job_title','bio']        

class UserRequestForm(UserCreationForm):
   
    class Meta:
        model= User
        exclude = ["email","password1","password2"]
        fields=["username"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ["profile"]
        fields = ["title","image","description","link"]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ["project","author"]
        fields = ["design","usability","content","average"]