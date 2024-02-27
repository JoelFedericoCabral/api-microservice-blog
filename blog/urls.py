from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, PostListCreateAPIView, PostDetailUpdateDeleteAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'), # URL para listar todos los posts.
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'), # URL para ver detalles de un post específico.
    path('posts/create/', PostListCreateAPIView.as_view(), name='post-create'),  # URL para crear un nuevo post.
    path('posts/update/<int:pk>/', PostDetailUpdateDeleteAPIView.as_view(), name='post-detail-update'),  # URL para modificar un post. Ya sea parcial (PATCH) o total (PUT).
    path('posts/delete/<int:pk>/', PostDetailUpdateDeleteAPIView.as_view(), name='post-detail-delete'),  # URL para eliminar un post.
]
