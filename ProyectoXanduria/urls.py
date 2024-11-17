"""
URL configuration for ProyectoXanduria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import index
    2. Add a URL to urlpatterns:  path('', index.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Importa el módulo admin para gestionar el panel de administración de Django
from django.urls import path, include  # Importa las funciones path e include para definir rutas

from tienda.api.router import router # Importa el objeto 'router' desde el módulo 'router' de la API de la tienda,
from drf_yasg import openapi  # los parámetros, respuestas y esquemas de la API en formato OpenAPI
from drf_yasg.views import get_schema_view # que genera automáticamente la documentación de la API en formato OpenAPI, facilitando la visualización y prueba de los endpoints.

schema_view = get_schema_view(
    openapi.Info(
        title='xanduria api',
        default_version='v1',
        description='documentacion de la api',
        terms_of_service="",
        contact=openapi.Contact(email='soporte.4ndr3s@gmail.com'),
        license=openapi.License(name='BSD Lincense'),
    ),
     public=True,
# permission_classes=(permissions.AllowAny,), 
)

urlpatterns = [  # Lista que contiene todas las rutas del proyecto
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('api/', include('user.api.roter')),
    path('api/', include(router.urls)),


    path('admin/', admin.site.urls),  # Ruta para acceder al panel de administración de Django
    path('', include('Principalapp.urls')),  # Incluye las rutas definidas en 'Principalapp.urls' para la ruta raíz
    path('contactenos/', include('Contactenos.urls')),  # Incluye las rutas definidas en 'Contactenos.urls' para la ruta raíz
    # path('registro/', include('registro.urls')),  # Incluye las rutas definidas en 'registro.urls' para la ruta raíz
    path('tienda/', include('tienda.urls')),  # Incluye las rutas definidas en 'tienda.urls' para la ruta raíz
    path('carro', include('carro.urls')),
    path('autenticacion/', include('autenticacion.urls')),
    path('pedidos/',include('pedidos.urls')),
    
]
