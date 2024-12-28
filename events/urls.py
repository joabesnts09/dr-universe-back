from django.urls import path
from .views import CreateListAllEventsView, GetUpdateDeleteEventsView


urlpatterns = [
    path('events/', CreateListAllEventsView.as_view(), name='create_events'),
    path(
        'events/<uuid:article_id>/',
        GetUpdateDeleteEventsView.as_view(),
        name='get_update_delete_events',
    ),
]
