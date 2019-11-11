from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='projects-home'),
    path('<int:project_id>/',views.uniqueP, name ='project'),
]