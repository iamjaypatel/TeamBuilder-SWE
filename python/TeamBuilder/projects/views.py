from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from login.models import Project, Profile
from projects.forms import createProjForm

# Create your views here.
def home(request):
    projects = Project.objects.all()
    data = {
        'projects': projects
    }
    return render(request,'projects/projhome.html', data)

def createProjView(request):
    if request.method == 'POST':
        form = createProjForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            newProj = Project() # Get Project values from form and profile object then save
            newProj.project_Admin = Profile.objects.get(profile_username = request.user.username)
            newProj.project_Name = form.cleaned_data['proj_name']
            newProj.project_Description = form.cleaned_data['proj_descr']
            newProj.project_SpaceAvailable = 9
            newProj.save()
            return HttpResponseRedirect('/projects/') # Returns to projects page **ToDo: add success alert, should be easy
    else:
        form = createProjForm()
    return render(request, 'projects/createProj.html', {'form': form})

def uniqueP(request, ID):
    # Query project ID and pass to page
    posts = Project.objects.get(project_id=ID)
    data = {
        'posts': posts
    }
    return render(request,'projects/project.html', data)