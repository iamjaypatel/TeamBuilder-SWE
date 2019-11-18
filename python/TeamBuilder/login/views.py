from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile
from login.forms import editProfForm

# Create your views here.
def index(request):
    return render(request,'login/index.html')

def myprof(request): # when clicking on "My Profile", gets profile of active user then loads page
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = editProfForm(request.POST)
            if form.is_valid(): # Edit profile form takes input values and saves them to the logged in users profile (!Not to their 'user'!)
                userProf = Profile.objects.get(profile_username = request.user.username)
                userProf.profile_firstName = form.cleaned_data['prof_firstName']
                userProf.profile_lastName = form.cleaned_data['prof_lastName']
                userProf.profile_Email = form.cleaned_data['prof_Email']
                userProf.save()
        else:
            form = editProfForm()
        curUser = Profile.objects.get(profile_username = request.user.username)
        return render(request, 'login/myprofile.html', {'form': form, 'curUser': curUser})
    else:
        return render(request,'login/')

def profile(request, username): # when username is searched through URL, if current user is logged-in find searched user and load profile page
    if request.user.is_authenticated:
        user = Profile.objects.get(profile_username = username)
        data = {
            'user':user
        }
        return render(request,'login/profile.html', data)
    else:
        return render(request,'login/')
