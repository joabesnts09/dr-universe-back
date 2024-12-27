from rest_framework import generics
from .serializers import ArticlesSerializer
from .models import Articles
from .permissions import ArticlesPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CreateArticleView(generics.CreateAPIView):
  queryset = Articles.objects.all()
  serializer_class = ArticlesSerializer
  
  
class GetUpdateDeleteArticleView(generics.RetrieveUpdateDestroyAPIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated, ArticlesPermission]
    
  queryset = Articles.objects.all()
  serializer_class = ArticlesSerializer
  