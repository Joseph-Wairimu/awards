from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileUpdateForm,  ProjectForm
from .models import  Profile, Project
from django.contrib.auth.decorators import login_required
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
    current_user = request.user
    if request.method == 'POST':
        form =ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
           project = form.save(commit=False)
           project.user = current_user
           project.save()          
        return redirect('profile')
    else:
            form = ProfileUpdateForm()
    return render(request, 'edit_profile.html', {"form": form})



def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


@login_required(login_url='login')  
def create_project(request):
    current_user = request.user
    if request.method == 'POST':
        form =ProjectForm(request.POST, request.FILES)
        if form.is_valid():
           project = form.save(commit=False)
           project.user = current_user
           project.save()
        return redirect('index')

    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {"form": form}) 
