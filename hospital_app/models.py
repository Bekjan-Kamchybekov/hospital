from django.contrib.auth.management.commands.changepassword import UserModel
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

class UserProfile(AbstractUser):
    USER_ROlE_CHOICES = (
        ('врач', 'Врач'),
        ('пациент', 'Пациент'),
        ('владелец больницы', 'Владелец больницы'),
    )
    user_role = models.CharField(max_length=20, choices=USER_ROlE_CHOICES, default='пациент')
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_image/')


    def __str__(self):
        return f'{self.username}'

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=30)
    owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    hospital_description = models.TextField()
    address = models.CharField(max_length=32)
    hospital_stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    hospital_video = models.FileField(upload_to='hospital_video/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.hospital_name}, {self.address}, {self.hospital_stars}'

class HospitalImage(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hospital_image/')

class DepartmentCategory(models.Model):
    department_name = models.CharField(max_length=20)

    def __str__(self):
        return self.department_name

class Doctor(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='doctor')
    speciality = models.CharField(max_length=20)
    department = models.ForeignKey(DepartmentCategory, on_delete=models.CASCADE)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    WEEK_DAYS = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )
    working_days = MultiSelectField(choices=WEEK_DAYS, max_length=50)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'Doctor {self.user}-{self.speciality}-{self.department}'

class PatientProfile(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='patient')
    emergency_contact = PhoneNumberField(region='KG', null=True, blank=True)
    BLOOD_TYPE_CHOICES = (
        ('O-', 'O Negative'),
        ('O+', 'O Positive'),
        ('A-', 'A Negative'),
        ('A+', 'A Positive'),
        ('B-', 'B Negative'),
        ('B+', 'B Positive'),
        ('AB-', 'AB Negative'),
        ('AB+', 'AB Positive'),
    )
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)

    def __str__(self):
        return f'Patient {self.user}-{self.emergency_contact}'


class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    STATUS_CHOICES = (
        ('запланировано', 'Запланировано'),
        ('завершено', 'Завершено'),
        ('отменено', 'Отменено'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='запланировано')

    def __str__(self):
        return f' Appointment for {self.patient} by {self.doctor} on {self.date_time}'

class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    prescribed_medication = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Record for {self.patient} by {self.doctor} on {self.created_at}'

class Feedback(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.doctor} by {self.patient} on {self.created_at}'

class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='message')
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='message_image/', null=True, blank=True)
    video = models.FileField(upload_to='message_video', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

