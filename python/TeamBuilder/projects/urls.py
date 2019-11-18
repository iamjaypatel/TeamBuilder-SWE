from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='projects-home'),
    path('<int:ID>/',views.uniqueP, name ='uProject'),
    path('<int:ID>/join/', views.joinP, name ='jProject'),
    path('createProj/', views.createProjView, name='createP'),
    path('myProjects/', views.myProjectsView, name='projects-my'),
]