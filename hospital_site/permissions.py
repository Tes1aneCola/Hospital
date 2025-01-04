from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'doctor_profile')

class IsPatient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'patient_profile')

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user
