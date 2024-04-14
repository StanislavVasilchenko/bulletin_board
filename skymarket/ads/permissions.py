# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Права доступа для пользователя, являющегося создателем объявления или комментария"""
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAdmin(permissions.BasePermission):
    """Права доступа для аоминистратора"""
    def has_permission(self, request, view):
        return request.user.role == 'admin'
