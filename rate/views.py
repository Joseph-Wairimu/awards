from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileUpdateForm
from .models import  Profile, Project
# Create your views here.

def index(request):
    projects= Project.objects.all()
   
    return render(request, 'index.html',{'projects': projects[::-1]})
  


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
   profile = Profile.objects.get(user=request.user)
   user = Profile.objects.get_or_create(user= request.user)
   form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
   bio = Profile.objects.get(user= request.user)
   image = Profile.objects.get(user= request.user)
   job_title = Profile.objects.get(user= request.user)
   if request.method == 'POST':
         form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
         if form.is_valid():
             
              profile.save()
         return redirect('profile')
   else:
            form = ProfileUpdateForm()
   return render(request, 'edit_profile.html', {"form": form, "user": user, "bio": bio, "image": image , "job_title": job_title})



def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})