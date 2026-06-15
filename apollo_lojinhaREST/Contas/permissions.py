from rest_framework.permissions import BasePermission, IsAuthenticated

class PermissionLojista(BasePermission):
    '''Checa a role da conta para liberar a permissão de lojista'''
    def has_permission(self, request, view):
        return request.user.role == 'L'
    
class PermissionCliente(BasePermission):
    '''Checa a role da conta para liberar a permissão de cliente'''
    def has_permission(self, request, view):
        return request.user.role == 'C'
    
class PermissionClienteSelf(BasePermission):
    """
    Permite acesso apenas ao próprio usuário ou Lojista.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.role == 'L'
    
