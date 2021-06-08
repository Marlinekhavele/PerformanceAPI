from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from .models import Performance
from .serializers import PerformanceSerializer

class PerformanceListView(generics.ListAPIView):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'