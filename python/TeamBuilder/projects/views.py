from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
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
        form = createProjForm
        return render(request, 'projects/createProj.html', {'form': form})

def uniqueP(request, ID):
    # Query project ID and pass to page
    proj = Project.objects.get(project_id=ID)
    members = Project_Involved.objects.filter(project_involved_id = proj)
    access = False
    involved = False
    if request.user.username == proj.project_Admin.profile_username:
        access = True
    inv = Project_Involved.objects.filter(project_involved_id = proj, project_involved_username = request.user.username)
    if inv:
        involved = True
    data = {
        'proj': proj,
        'members': members,
        'access': access,
        'involved': involved
    }
    return render(request,'projects/project.html', data)

def myProjectsView(request):
    # Get all projects with current user as admin, display on projects page
    if request.user.is_authenticated:
        curProfile = Profile.objects.get(profile_username = request.user.username)
        #projects = Project.objects.filter(project_Admin = curProfile)
        projlist = Project_Involved.objects.filter(project_involved_username = curProfile) # Set of Project_Involved for current profile
        projects = []
        for p in projlist:
            projects.append(p.project_involved_id) # for every Project_Involved entry, pull Project object, put into list of Project objects
        data = {
            'projects': projects
        }
        return render(request, 'projects/projhome.html', data)
    else:
        return render(request, 'login/index.html')

def joinP(request, ID):
    if request.user.is_authenticated:
        project = Project.objects.get(project_id = ID)

        if not project:
            print()
            # ToDo: add failure alert: project does not exist

        elif project.project_SpaceAvailable <= 0:
            print()
            # ToDo: add failure alert: no space available

        elif Project_Involved.objects.filter(project_involved_id = project, project_involved_username = request.user.username):
            print()
            # ToDo: add failure alert: already in project

        else:
            pie = Project_Involved() # Project-Involved Entry
            pie.project_involved_username = Profile.objects.get(profile_username = request.user.username)
            pie.project_involved_id = project
            pie.project_involved_accepted = False
            pie.save()
            project.project_SpaceTaken = project.project_SpaceTaken + 1
            project.project_SpaceAvailable = project.project_SpaceAvailable - 1
            project.save()
        # Check space, add project_involved entry

        return HttpResponseRedirect('/projects/myProjects/')
    else:
        return render(request, 'login/')


def acceptP(request, ID, username):
    if request.user.is_authenticated:
        involved = Project_Involved.objects.filter(project_involved_id = ID, project_involved_username = username)
        if involved:
            involved = Project_Involved.objects.get(project_involved_id = ID, project_involved_username = username)
            involved.project_involved_accepted = True
            involved.save()
        return HttpResponseRedirect('/projects/' + str(ID))
    else:
        return render(request, 'login/')

def rejectP(request, ID, username):
    if request.user.is_authenticated:
        involved = Project_Involved.objects.filter(project_involved_id = ID, project_involved_username = username)
        if involved:
            involved = Project_Involved.objects.get(project_involved_id = ID, project_involved_username = username)
            proj = involved.project_involved_id
            proj.project_SpaceAvailable = proj.project_SpaceAvailable + 1
            proj.project_SpaceTaken = proj.project_SpaceTaken - 1
            proj.save()
            involved.delete()
        return HttpResponseRedirect('/projects/' + str(ID))
    else:
        return render(request, 'login/')

def leaveP(request, ID):
    if request.user.is_authenticated:
        involved = Project_Involved.objects.filter(project_involved_id = ID, project_involved_username = request.user.username)
        if involved:
            involved = Project_Involved.objects.get(project_involved_id = ID, project_involved_username = request.user.username)
            proj = involved.project_involved_id
            proj.project_SpaceAvailable = proj.project_SpaceAvailable + 1
            proj.project_SpaceTaken = proj.project_SpaceTaken - 1
            proj.save()
            involved.delete()
        return HttpResponseRedirect('/projects/')
    else:
        return render(request, 'login/')

def deleteP(request, ID):
    if request.user.is_authenticated:
        proj = Project.objects.get(project_id = ID)
        if(proj.project_Admin.profile_username == request.user.username):
            involved = Project_Involved.objects.filter(project_involved_id = ID)
            for i in involved:
                i.delete()
            proj.delete()
        return HttpResponseRedirect('/projects/')
    else:
        return render(request, 'login/')