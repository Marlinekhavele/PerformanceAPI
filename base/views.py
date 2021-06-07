from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Performance
from .serializers import PerformanceSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

    def list(self, request):
        queryset = Performance.objects.all()
        serializer = PerformanceSerializer(queryset, many=True)
        return Response(serializer.data)