from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('career/<int:career_id>',views.detail, name='detail'),
    # path('jobs', views.jobs, name='jobs'),
    path('job/<int:job_id>', views.jobdetail, name='jobdetail'),
    # path('add/', views.addjobs, name='addjobs'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]