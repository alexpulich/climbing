from rest_framework import viewsets
from ..models import TrainingDay
from .serializers import TrainingDaySerializer


class TrainingDayViewSet(viewsets.ModelViewSet):
    queryset = TrainingDay.objects.all()
    serializer_class = TrainingDaySerializer
