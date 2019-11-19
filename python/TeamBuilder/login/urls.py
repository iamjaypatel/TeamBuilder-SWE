from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='login-user'),
    path('/<str:username>/', views.profile , name='user-page'),
    path('mypage/', views.myprof, name='my-page'),
    path('logout/', views.logout_view, name='logout'),
    path("register/", views.register, name="register"),
]