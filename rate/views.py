from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileUpdateForm
from .models import  Profile
# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():

            form.save()
           
            
            return redirect('login')
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})

def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)

def edit_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    if request.method == 'POST':
        form =  ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})   