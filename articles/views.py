from rest_framework import generics
from .serializers import ArticlesSerializer
from .models import Articles
from .permissions import ArticlesPermission, ConditionalJWTAuthentication


class CreateListAllArticleView(generics.ListCreateAPIView):
    permission_classes = [ArticlesPermission]
    authentication_classes = [ConditionalJWTAuthentication]
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class GetUpdateDeleteArticleView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ArticlesPermission]
    authentication_classes = [ConditionalJWTAuthentication]

    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    lookup_url_kwarg = "article_id"
