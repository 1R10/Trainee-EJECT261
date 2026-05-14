from django.contrib import admin
from django.urls import path
from Contas.views import Contas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Contas/', Contas),
]
