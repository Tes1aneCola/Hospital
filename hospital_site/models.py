from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('doctor', 'Врач'),
        ('patient', 'Пациент'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    speciality = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    working_days = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.speciality}"



class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    blood_type = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.user.first_name



class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Запланировано'),
        ('completed', 'Завершено'),
        ('cancelled', 'Отменено'),
    ]
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    date_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"{self.doctor}-{self.date_time}"



class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='medical_records')
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescribed_medication = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient}-{self.doctor}-{self.created_at}"



class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='feedback')
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='feedback')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor}-{self.patient}"

