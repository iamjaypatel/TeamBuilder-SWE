from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='projects-home'),
    path('11111/', views.unique, name='project'),
    path('<int:project_id>/',views.uniqueP, name ='uProject'),
]