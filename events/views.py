from rest_framework import generics
from articles.permissions import ConditionalJWTAuthentication
from .serializers import EventsSerializer
from .models import Events
from .permissions import EventsPermission
from rest_framework.response import Response
from rest_framework import status


class CreateListAllEventsView(generics.ListCreateAPIView):
  authentication_classes = [ConditionalJWTAuthentication]
  permission_classes = [EventsPermission]
  queryset = Events.objects.all()
  serializer_class = EventsSerializer
  
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
  
  
class GetUpdateDeleteEventsView(generics.RetrieveUpdateDestroyAPIView):
  authentication_classes = [ConditionalJWTAuthentication]
  permission_classes = [EventsPermission]
    
  queryset = Events.objects.all()
  serializer_class = EventsSerializer
  lookup_url_kwarg = 'events_id'