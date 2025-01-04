from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'records', MedicalRecordViewSet, basename='medicalrecord')
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),]