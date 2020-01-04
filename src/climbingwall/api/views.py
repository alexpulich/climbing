from rest_framework import viewsets
from ..models import Climbingwall
from .serializers import ClimbingwallSerializer


class ClimbingwallViewSet(viewsets.ModelViewSet):
    queryset = Climbingwall.objects.all()
    serializer_class = ClimbingwallSerializer
