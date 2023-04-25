"""
dados pora inserir imagens + static settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
precisar ir la o settings finalizar a configutação
"""
from django.contrib import admin
from django.urls import path, include

#Inserir imagens
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        path('', include('contatos.urls')),
        path('accounts/', include('accounts.urls')),
        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
