from rest_framework import generics, status, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


class PostListAPIView(generics.ListAPIView): # Una vista de API que muestra una lista de todos los posts.
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveAPIView): # Una vista de API que muestra los detalles de un post específico.
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView): # Una vista de API que permite listar y crear posts.
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Solo usuarios autenticados pueden crear posteos. Luego se puede cambiar para restringir mas el acceso a la creacion de posts.

    def post(self, request, *args, **kwargs): # Método para crear un nuevo post.
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView): # Una vista de API que permite ver, actualizar y eliminar un post.
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs): # Metodo para eliminar post.
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs): # Metodo para actualizar post.
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def patch(self, request, *args, **kwargs): # Metodo para realizar la actualizacion parcial de un post.
        return self.partial_update(request, *args, **kwargs)