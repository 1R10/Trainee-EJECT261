from django.apps import AppConfig


class PedidosConfig(AppConfig):
    name = 'Pedidos'

    def ready(self):
        import Pedidos.signals