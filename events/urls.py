from django.urls import path
from .views import CreateEventsView, GetUpdateDeleteEventsView


urlpatterns = [
    path("articles/", CreateEventsView.as_view(), name='create_events'),
    path(
        "articles/<uuid:article_id>/",
        GetUpdateDeleteEventsView.as_view(),
        name='get_update_delete_events'
    ),
]