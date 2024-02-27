from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer): # Serializador para convertir objetos Post en representaciones JSON y viceversa.
    class Meta:
        model = Post # El modelo que se va a serializar/deserializar.
        fields = ('id', 'title', 'caption', 'content', 'image', 'author', 'created', 'updated') # Los campos del modelo que se incluirán en la serialización.
        read_only_fields = ('created', 'updated') # Los campos de solo lectura que no se pueden modificar durante la deserialización. Siempre es una tupla, asi que si tiene un solo elemento asegurate de ponerle la "," al ultimo.
