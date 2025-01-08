from rest_framework.permissions import BasePermission
from rest_framework import permissions

# Doctor
class CheckDoctor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class CheckHospitalOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class CheckMedicalRecords(BasePermission):
    def has_permission(self, request, obj):
        if request.user.user_role == 'пациент':
            return False
        return True

# Patient

class CheckPatientReview(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_name == request.user

class CheckAppointment(BasePermission):
    def has_permission(self, request, obj):
        if request.user.user_role == 'врач':
            return False
        return True

class CheckMedicalRecordOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user