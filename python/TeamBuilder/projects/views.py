from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'projectID': '11111',
        'projectAdmin': 'Sam',
        'projectName': 'Deliverable5',
        'descr': 'Insert description here',
        'maxCap': '10',
        'spaceTaken': '1',
        'spaceAvailable': '9'
    },
    {
        'projectID': '22222',
        'projectAdmin': 'Jon',
        'projectName': 'Database Stuff',
        'descr': 'Another description here',
        'maxCap': '10',
        'spaceTaken': '5',
        'spaceAvailable': '5'
    }
]

# Create your views here.
def home(request):
    data = {
        'posts': posts
    }
    return render(request,'projects/projhome.html', data)

def unique(request):
    posts = {
        'projectID':'11111',
        'projectAdmin':'Sam',
        'projectName': 'Deliverable5',
        'descr': 'Insert description here',
        'maxCap': '10',
        'spaceTaken': '1',
        'spaceAvailable': '9' 
    }
    data = {
        'posts': posts
    }
    return render(request,'projects/project.html', data)

def uniqueP(request, project_id):
    # we will be doing same as unique but instead will query for the project
    posts = {
        'projectID': project_id,
        'projectAdmin':'Sam',
        'projectName': 'Deliverable5',
        'descr': 'Insert description here',
        'maxCap': '10',
        'spaceTaken': '1',
        'spaceAvailable': '9' 
    }
    data = {
        'posts': posts
    }
    return render(request,'projects/project.html', data)