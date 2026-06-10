from rest_framework.permissions import BasePermission

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
    Permite que o cliente apenas visualize contaPadrao se for o dono.
    Bloqueia request se não for o dono da conta.
    """
    
    def has_object_permission(self, request, view, obj):
        '''
        Só retorna true se user = pessoa logada
        '''
        print('RODOU --------------- AQUIIII ALOOO')

        return obj == request.user or request.user.role == 'L'
    
