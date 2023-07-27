from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Snack
from .permissions import IsOwnerOrReadOnly
from .serializers import SnacksSerializer


class SnackList(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnacksSerializer


class SnackDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnacksSerializer
