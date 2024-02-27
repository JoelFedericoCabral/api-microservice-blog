from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=100)
    content = models.CharField(max_length=800)
    image = models.ImageField(upload_to='miniblog', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #Campo que representa al autor del post. Es una clave externa que apunta al modelo de usuario predeterminado de Django.
    #Cuando se elimina un usuario, todos los posts asociados a ese usuario también se eliminan (CASCADE).
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post' # Nombre verbose para un solo objeto de este modelo.
        verbose_name_plural = 'posts' # Nombre verbose para la colección de objetos de este modelo.

    def __str__(self):
        return self.title
