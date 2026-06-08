from rest_framework.permissions import BasePermission

class PermissionLojista(BasePermission):
    '''Checa a role da conta para liberar a permissão de lojista'''
    def has_permission(self, request, view):
        return request.user.role == 'L'
    
class PermissionCliente(BasePermission):
    '''Checa a role da conta para liberar a permissão de cliente'''
    def has_permission(self, request, view):
        return request.user.role == 'C'
    
