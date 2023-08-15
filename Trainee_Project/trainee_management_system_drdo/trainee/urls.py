from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('add_trainee/', views.add_trainee, name='add_trainee'),
    path('enroll_trainee/', views.enroll_trainee, name='enroll_trainee'),
    path('trainee_list/', views.trainee_list, name='trainee_list'),
    path('course_list/', views.course_list, name='course_list'),
    path('trainer_list/', views.trainer_list, name='trainer_list'),
    path('enrollments/', views.enrollments, name='enrollments'),
    path('add_course/', views.add_course, name='add_course'),
    path('training_center_list/', views.training_center_list, name='training_center_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
