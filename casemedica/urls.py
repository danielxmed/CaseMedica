from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # 'core' será nossa aplicação principal
    path('usuarios/', include('usuarios.urls')),
]
