from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login-projects'),
    path('u/<str:username>/', views.profile , name='user-page'),
    path('mypage/', views.myprof, name='my-page'),
]