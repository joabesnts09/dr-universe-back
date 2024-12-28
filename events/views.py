from rest_framework import generics
from articles.permissions import ConditionalJWTAuthentication
from .serializers import EventsSerializer
from .models import Events
from .permissions import EventsPermission


class CreateListAllEventsView(generics.ListCreateAPIView):
  authentication_classes = [ConditionalJWTAuthentication]
  permission_classes = [EventsPermission]
  queryset = Events.objects.all()
  serializer_class = EventsSerializer
  
  
class GetUpdateDeleteEventsView(generics.RetrieveUpdateDestroyAPIView):
  authentication_classes = [ConditionalJWTAuthentication]
  permission_classes = [EventsPermission]
    
  queryset = Events.objects.all()
  serializer_class = EventsSerializer
  lookup_url_kwarg = 'events_id'