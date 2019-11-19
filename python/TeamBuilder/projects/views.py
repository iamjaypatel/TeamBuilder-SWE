from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from login.models import Project, Profile, Project_Involved
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
            newPIE = Project_Involved()
            newPIE.project_involved_username = Profile.objects.get(profile_username = request.user.username)
            newPIE.project_involved_id = newProj
            newPIE.project_involved_accepted = True # Default acceptance for Admin is true
            newPIE.save()
        return HttpResponseRedirect('/projects/') # Returns to projects page **ToDo: add success alert, should be easy
    else:
        return render(request, 'projects/createProj.html', {'form': form})

def uniqueP(request, ID):
    # Query project ID and pass to page
    proj = Project.objects.get(project_id=ID)
    members = Project_Involved.objects.filter(project_involved_id = proj) # Query of project_involved entries for given project
    memlist = []
    for m in members:
        memlist.append(Profile.objects.get(m.project_involved_username))
    data = {
        'proj': proj,
        'memlist': memlist
    }
    return render(request,'projects/project.html', data)

def myProjectsView(request):
    # Get all projects with current user as admin, display on projects page
    if request.user.is_authenticated:
        curProfile = Profile.objects.get(profile_username = request.user.username)
        projects = Project.objects.filter(project_Admin = curProfile)
        data = {
            'projects': projects
        }
        return render(request, 'projects/projhome.html', data)
    else:
        return render(request, 'login/')

def joinP(request, ID):
    if request.user.is_authenticated:
        project = Project.objects.get(project_id = ID)

        if not project:
            print()
            # ToDo: add failure alert

        elif project.project_SpaceAvailable <= 0:
            print()
            # ToDo: add failure alert

        else:
            pie = Project_Involved() # Project-Involved Entry
            pie.project_involved_username = Profile.
            pie.project_involved_id =
            pie.project_involved_accepted
            pie.save()
        # Check space, add project_involved entry

        return HttpResponseRedirect('/projects/myProjects/')
    else:
        return render(request, 'login/')
