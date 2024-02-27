from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Ruta para acceder al panel de administración de Django
    path('api/', include('blog.urls')),  # Incluye las URLs de la app 'blog'
]
