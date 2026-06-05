from rest_framework import permissions

class IsAdminOrPsicologoOrReadOnly(permissions.BasePermission):
    """
    Permite acceso de solo lectura (GET, HEAD, OPTIONS) a cualquier usuario autenticado.
    Permite acceso de escritura/edición/eliminación solo a administradores o psicólogos.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
            
        if request.method in permissions.SAFE_METHODS:
            return True
            
        is_psicologo = hasattr(request.user, 'psicologo')
        return request.user.is_staff or is_psicologo

class IsAdminOrPsicologoOrCanCreateCertain(permissions.BasePermission):
    """
    Permite acceso de solo lectura o creación (POST) a cualquier usuario autenticado.
    Permite edición y eliminación (PUT, PATCH, DELETE) solo a administradores o psicólogos.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
            
        if request.method in permissions.SAFE_METHODS or request.method == 'POST':
            return True
            
        is_psicologo = hasattr(request.user, 'psicologo')
        return request.user.is_staff or is_psicologo
