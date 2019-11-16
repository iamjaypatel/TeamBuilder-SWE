from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='projects-home'),
    path('<int:ID>/',views.uniqueP, name ='uProject'),
    path('createProj', views.createProjView, name='createP'),
]