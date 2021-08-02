from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from artistas.api.viewsets import ArtistaViewSet, EventoArtistaViewSet
from bares.api.viewsets import BarViewSet
from bebidas.api.viewsets import BebidaViewSet
from comidas.api.viewsets import ComidaViewSet
from empresa.api.viewsets import EmpresaViewSet
from eventos.api.viewsets import EventoViewSet
from ingressos.api.viewsets import IngressoViewSet
from perfil_empresa.api.viewsets import PerfilEmpresaViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'artistas', ArtistaViewSet)
router.register(r'evento_artista', EventoArtistaViewSet)
router.register(r'bar', BarViewSet)
router.register(r'bebida', BebidaViewSet)
router.register(r'comida', ComidaViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'evento', EventoViewSet)
router.register(r'ingressos', IngressoViewSet)
router.register(r'perfil_empresa', PerfilEmpresaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('eventos.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('retorno/pagseguro/', include('pagseguro.urls'))
]

