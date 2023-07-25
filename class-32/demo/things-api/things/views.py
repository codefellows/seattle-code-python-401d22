from rest_framework import generics
from .serializer import ThingSerializer
from .models import Thing
from .permissions import IsOwnerOrReadOnly


class ThingList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


