from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'User-profiles', UserProfileViewSet, basename='user-profile')
router.register(r'Hospitals', HospitalViewSet, basename='hospital')
router.register(r'Hospital-images', HospitalImageViewSet, basename='hospital-image')
router.register(r'Department-categories', DepartmentCategoryViewSet, basename='department-categories')
router.register(r'Doctor', DoctorListViewSet, basename='doctor-list')
router.register(r'Doctor-detail', DoctorDetailViewSet, basename='doctor-detail')
# router.register(r'Patients', PatientProfileViewSet, basename='patient')
router.register(r'Appointments', AppointmentViewSet, basename='appointment')
# router.register(r'Medical-records', MedicalRecordViewSet, basename='medical-records')
router.register(r'Feedbacks', FeedbackViewSet, basename='feedback')


urlpatterns = [
    path('', include(router.urls)),
    path('medical_records/', MedicalRecordListAPIView.as_view(), name='medical-records-list'),
    path('medical_records/<int:pk>/', MedicalRecordDetailListAPIView.as_view(), name='medical-records-detail'),
    path('patient_profiles/', PatientProfileListCreateView.as_view(), name='patient-profiles-list-create'),

    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),

]
