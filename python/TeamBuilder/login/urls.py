from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='login-user'),
    path('u/<str:username>/', views.profile , name='user-page'),
    path('logout/', views.logout_view, name='logout'),
    path("register/", views.register, name="register"),
    path("help/", views.help, name="help")
]