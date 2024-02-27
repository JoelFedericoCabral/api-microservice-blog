from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated') # Campos que serán de solo lectura en el panel de administración.

admin.site.register(Post, PostAdmin)