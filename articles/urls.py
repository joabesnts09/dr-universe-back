from django.urls import path
from .views import CreateArticleView, GetUpdateDeleteArticleView


urlpatterns = [
    path("articles/", CreateArticleView.as_view(), name='create_article'),
    path(
        "articles/<uuid:article_id>/",
        GetUpdateDeleteArticleView.as_view(),
        name='get_update_delete_article'
    ),
]