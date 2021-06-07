from rest_framework import serializers
from .models import Performance

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','channel','country','os','impressions','clicks','installs','spend','revenue']
        model = Performance