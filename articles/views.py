from rest_framework import generics
from .serializers import ArticlesSerializer
from .models import Articles
from .permissions import ArticlesPermission, ConditionalJWTAuthentication
from rest_framework.response import Response
from rest_framework import status


class CreateListAllArticleView(generics.ListCreateAPIView):
    permission_classes = [ArticlesPermission]
    authentication_classes = [ConditionalJWTAuthentication]
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super().get_serializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetUpdateDeleteArticleView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ArticlesPermission]
    authentication_classes = [ConditionalJWTAuthentication]

    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    lookup_url_kwarg = "article_id"
