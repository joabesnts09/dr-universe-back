from rest_framework import generics
from .serializers import EventsSerializer
from .models import Events
from .permissions import EventsPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CreateEventsView(generics.CreateAPIView):
  queryset = Events.objects.all()
  serializer_class = EventsSerializer
  
  
class GetUpdateDeleteEventsView(generics.RetrieveUpdateDestroyAPIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated, EventsPermission]
    
  queryset = Events.objects.all()
  serializer_class = EventsSerializer
  lookup_url_kwarg = 'events_id'