from django.urls import path
from .views import CreateArticleView, GetUpdateDeleteArticleView


urlpatterns = [
    path("articles/", CreateArticleView.as_view()),
    path(
        "articles/<uuid:course_id>/",
        GetUpdateDeleteArticleView.as_view(),
    ),
]