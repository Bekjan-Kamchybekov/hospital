from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken


from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('username', 'email', 'password', 'first_name', 'last_name',
#                   'phone_number')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = Profile.objects.create_user(**validated_data)
#         return user
#
#
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#
#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError('Неверные учетные данные')
#
#     def to_representation(self, instance):
#         refresh = RefreshToken.for_user(instance)
#         return {
#             'user': {
#                 'username': instance.username,
#                 'email': instance.email,
#             },
#             'access': str(refresh.access_token),
#             'refresh': str(refresh),
#         }

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'profile_picture']

class HospitalSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(read_only=True)
    class Meta:
        model = Hospital
        fields = ['hospital_name', 'owner', 'hospital_description', 'address', 'hospital_stars', 'hospital_video', 'created_date']

class HospitalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalImage
        fields = ['id', 'hospital', 'image']

class DepartmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentCategory
        fields = ['id', 'department_name']


class DoctorListSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'speciality', 'working_days']

class DoctorDetailSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)
    department = DepartmentCategorySerializer(read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'speciality', 'department', 'shift_start', 'shift_end', 'working_days', 'price']

class PatientProfileSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = PatientProfile
        fields = ['id', 'user', 'emergency_contact', 'blood_type']

class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientProfileSerializer(read_only=True)
    doctor = DoctorListSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date_time', 'status']

class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = PatientProfileSerializer(read_only=True)
    doctor = DoctorListSerializer(read_only=True)

    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'doctor', 'created_at']

class MedicalRecordDetailSerializer(serializers.ModelSerializer):
    patient = PatientProfileSerializer(read_only=True)
    doctor = DoctorListSerializer(read_only=True)

    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'doctor', 'diagnosis', 'treatment', 'prescribed_medication', 'created_at']

class FeedbackSerializer(serializers.ModelSerializer):
    patient = PatientProfileSerializer(read_only=True)
    doctor = DoctorListSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'patient', 'doctor', 'rating', 'comment', 'created_at']