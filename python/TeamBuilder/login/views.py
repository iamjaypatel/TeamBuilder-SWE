from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Profile
from login.forms import editProfForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect(index)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            newP = Profile()
            newP.profile_username = form.cleaned_data['username']
            newP.profile_password = form.cleaned_data['password1']
            newP.save()
            user = form.save()
            login(request, user)
            return redirect(index)
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,template_name = "login/register.html",context={"form":form})
    form = UserCreationForm
    return render(request = request,template_name = "login/register.html",context={"form":form})


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/projects/')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect('/projects/')
        ...
    else:
        # Return an 'invalid login' error message.
        ...
    return render(request,'login/index.html')

# def myprof(request): # when clicking on "My Profile", gets profile of active user then loads page
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = editProfForm(request.POST)
#             if form.is_valid(): # Edit profile form takes input values and saves them to the logged in users profile (!Not to their 'user'!)
#                 userProf = Profile.objects.get(profile_username = request.user.username)
#                 userProf.profile_firstName = form.cleaned_data['prof_firstName']
#                 userProf.profile_lastName = form.cleaned_data['prof_lastName']
#                 userProf.profile_Email = form.cleaned_data['prof_Email']
#                 userProf.save()
#         else:
#             form = editProfForm()
#         curUser = Profile.objects.get(profile_username = request.user.username)
#         return render(request, 'login/myprofile.html', {'form': form, 'curUser': curUser})
#     else:
#         return render(request,'login/')

def profile(request, username): # when username is searched through URL, if current user is logged-in find searched user and load profile page
    if request.method == 'POST':
        form = editProfForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            userView = Profile.objects.get(profile_username = username)
            userView.profile_firstName = form.cleaned_data['prof_firstName']
            userView.profile_lastName = form.cleaned_data['prof_lastName']
            userView.profile_Email = form.cleaned_data['prof_Email']
            userView.save()
            return redirect(index)
    if request.user.is_authenticated:
        editAccess = False
        userView = Profile.objects.get(profile_username = username)

        if userView.profile_username == request.user.username:
            editAccess = True
        form = editProfForm
        data = {
            'userView':userView,
            'access':editAccess,
            'form':form
        }
       
        return render(request,'login/profile.html', data)
    else:
        return render(request,'login/')

def help(request):
    return render(request, 'login/help.html')