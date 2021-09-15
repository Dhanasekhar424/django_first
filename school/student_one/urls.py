from django.urls import path
from student_one import views

urlpatterns = [
    path('',views.happy,name='happy'),
    path('home',views.home,name='home'),
    path('mail',views.mail,name='mail'),
    path('information',views.information,name='information'),
    path('trainee',views.trainee,name='trainee'),
    
]