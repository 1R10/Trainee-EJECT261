from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from Contas.permissions import PermissionLojista
from suporte.models import ContatarSuporte
from suporte.serializers import SuporteSerializer

class SuporteViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        self.permission_classes = [AllowAny] 
        return super().get_permissions()

    queryset = ContatarSuporte.objects.all().order_by('id')
    serializer_class = SuporteSerializer