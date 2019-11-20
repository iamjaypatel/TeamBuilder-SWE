from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='projects-home'),
    path('<int:ID>/',views.uniqueP, name ='uProject'),
    path('<int:ID>/join/', views.joinP, name ='jProject'),
    path('<int:ID>/leave/', views.leaveP, name='lProject'),
    path('<int:ID>/delete/', views.deleteP, name='dProject'),
    path('<int:ID>/a/<str:username>', views.acceptP, name='aProject'),
    path('<int:ID>/r/<str:username>', views.rejectP, name='rProject'),
    path('createProj/', views.createProjView, name='createP'),
    path('myProjects/', views.myProjectsView, name='projects-my'),
]