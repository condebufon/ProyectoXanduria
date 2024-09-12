from django.urls import path
from registro import views



from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    
    path('registro', views.registro, name="registro"),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)