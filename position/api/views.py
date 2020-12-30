from rest_framework import generics

from .models import Position
from .serializers import PositionSerializer


class PositionViewDetail(generics.RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionViewList(generics.ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
