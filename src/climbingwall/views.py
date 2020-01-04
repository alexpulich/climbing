from rest_framework import viewsets
from climbingwall.models import Climbingwall
from climbingwall.serializers import ClimbingwallSerializer


class ClimbingwallViewSet(viewsets.ModelViewSet):
    queryset = Climbingwall.objects.all()
    serializer_class = ClimbingwallSerializer
