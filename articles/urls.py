from django.urls import path
from .views import CreateListAllArticleView, GetUpdateDeleteArticleView


urlpatterns = [
    path("articles/", CreateListAllArticleView.as_view(), name='create_article'),
    path(
        "articles/<uuid:article_id>/",
        GetUpdateDeleteArticleView.as_view(),
        name='get_update_delete_article'
    ),
]