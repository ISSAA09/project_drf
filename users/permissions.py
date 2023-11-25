from rest_framework.permissions import BasePermission

from education.models import Subscriber
from users.models import UserRole


class IsMember(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == UserRole.MEMBER:
            return True


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == UserRole.MODERATOR:
            return True
        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsSubscriber(BasePermission):
    def has_permission(self, request, view):
        if Subscriber.is_active_subscription:
            return True
