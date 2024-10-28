# data_processor/serializers.py
from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    inferred_data = serializers.DictField()
