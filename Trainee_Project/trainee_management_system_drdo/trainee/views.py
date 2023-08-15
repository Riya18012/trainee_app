from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trainee, Course, Trainer, TrainingCenter, Enrollment
from .forms import TraineeForm, EnrollmentForm, CourseForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL
        else:
            error_message = "Invalid username or password."
            return render(request, 'trainee/login.html', {'error_message': error_message})
    return render(request, 'trainee/login.html')

# dashboard


def dashboard(request):
    return render(request, 'trainee/dashboard.html')


def add_trainee(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trainee added successfully!')
            return redirect('trainee_list')  # Redirect to trainee list page after successful submission
    else:
        form = TraineeForm()

    return render(request, 'trainee/add_trainee.html', {'form': form})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a relevant page or display a success message
            return redirect('course_list')  # Redirect to the course list view
    else:
        form = CourseForm()
    return render(request, 'trainee/add_course.html', {'form': form})


def enrollments(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'trainee/enrollments.html', {'enrollments': enrollments})


def enroll_trainee(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'enrolled successfully!')
            return redirect('enrollments')  # Redirect to trainee list page after successful submission
            # Redirect or display success message
    else:
        form = EnrollmentForm()
    return render(request, 'trainee/enroll_trainee.html', {'form': form})


def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'trainee/course_list.html', {'courses': courses})


def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainee/trainer_list.html', {'trainers': trainers})


def training_center_list(request):
    centers = TrainingCenter.objects.all()
    return render(request, 'trainee/training_center_list.html', {'centers': centers})