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

   user = request.user
   user = Profile.objects.get_or_create(user= request.user)
   bio = Profile.objects.get(user= request.user)
   image = Profile.objects.get(user= request.user)
   job_title = Profile.objects.get(user= request.user)
   if request.method == 'POST':
         form = ProfileUpdateForm(request.POST, request.FILES)
         if form.is_valid():
              profile = form.save(commit=False)
              profile.user = user
              profile.save()
         return redirect('profile')
   else:
            form = ProfileUpdateForm()
   return render(request, 'edit_profile.html', {"form": form, "user": user, "bio": bio, "image": image , "job_title": job_title})
