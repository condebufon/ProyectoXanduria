from django.urls import path
from Contactenos import views


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('contactenos', views.contacto, name="contactenos"),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)