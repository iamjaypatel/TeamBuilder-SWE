from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'login/index.html')

# def profile(request,username):
#     info = {
#         'username':username,
#         'email':'test@temp.com',
#     }
#     data ={
#         'info':info
#     }
#     return render(request,'login/profile.html',info)
