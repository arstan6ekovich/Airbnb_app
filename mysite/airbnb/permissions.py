from rest_framework.permissions import BasePermission

class GuestPermission (BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'guest'


class HostPermission (BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'host'


class AdminPermission (BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'