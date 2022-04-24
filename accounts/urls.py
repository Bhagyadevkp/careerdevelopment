from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    # path('studentregister', views.studentregister, name='studentregister'),
    path('register_company',views.register_company,name='register_company'),
    # path('userdetails',views.userdetails,name='userdetails'),
]