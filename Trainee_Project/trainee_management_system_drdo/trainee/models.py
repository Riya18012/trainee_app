from django.db import models
# Create your models here.


class TrainingCenter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_email = models.EmailField(null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    training_center = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Trainee(models.Model):
    trainee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone_num = models.CharField(max_length=15)
    address = models.TextField(null=True)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)  # Add a primary key field
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    training_period = models.PositiveIntegerField()  # Add a field for training period (in months)

    def __str__(self):
        return f"{self.trainee.name} - {self.course.name}"

