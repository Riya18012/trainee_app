from django import forms
from .models import Trainee, Enrollment, Course


class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = '__all__'


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
